from django.shortcuts import render
from .models import Client, Appointment, TimeSlots, Service
from home.models import Regi_key
from notifications.notify_fms import Notify
from owner.models import Salon_token_ids
from datetime import datetime, timedelta, time
import time as time_conv
from django.db.models import Q
# Create your views here.


def appointment_index(request):
    if request.POST:
        cli_name = request.POST['cli_name']
        cli_number = request.POST['cli_number']
        cli_services = request.POST['cli_services']
        cli_time = request.POST['cli_time'].split('%')
        cli_token = request.POST['cli_token']
        if len(Client.objects.filter(number=cli_number)) == 0:
            # create cli
            cli = Client.objects.create(name=cli_name, number=cli_number)
            regi_token = Regi_key.objects.filter(token=cli_token)
            if len(regi_token) == 0:
                Regi_key.objects.create(token=cli_token, cli=cli)
            else:
                for token in regi_token:
                    token.cli = cli
                    token.save()
        else:
            cli = Client.objects.get(number=cli_number)
            regi_token = Regi_key.objects.filter(token=cli_token)
            if len(regi_token) == 0:
                Regi_key.objects.create(token=cli_token, cli=cli)
            else:
                for token in regi_token:
                    token.cli = cli
                    token.save()
        cli_time_format = time_conv.strptime(cli_time[0], "%H:%M %p")
        Appointment.objects.create(
            time=f'{cli_time_format.tm_hour}:{cli_time_format.tm_min}', date=f'{cli_time[1]}', confirmation=False, work_to_be_done=cli_services, cli=cli)
        tokens = Salon_token_ids.objects.all()
        to_notify_tokens = []
        for token in tokens:
            to_notify_tokens.append(token.token)
        admin_notify = Notify(to_notify_tokens)
        admin_notify.send_admin_prompt(
            cli_name=cli_name, cli_date='temp[1]', cli_services=cli_services)

        return render(request, 'appointment/thank-you.html')
        #  get the data and send a notification to the admins and put the appointment on pending.
        # slot timings PENDING
    today = datetime.today().date()
    today_1 = datetime.today() + timedelta(days=1)
    today_2 = datetime.today() + timedelta(days=2)
    today_3 = datetime.today() + timedelta(days=3)
    days = [today, today_1.date(), today_2.date(), today_3.date()]
    time_selection = []  # THIS OBJ IS PASSED TO THE TEMPLATES TO RENDER
    start_time = datetime(1, 1, 1, 11, 00, 00)
    time_list = [start_time]  # LIST OF ALL TIME SLOTS
    for i in range(18):
        start_time = start_time + timedelta(minutes=30)
        time_list.append(start_time)
    for day in days:
        # obj structure = {'date':date, 'time':time}
        if day == datetime.today().date():
            # 3 cases where the client is either before the working hours or after the working hours or during the working hours
            if datetime.now().time() <= time(11, 0, 0):
                # show entire day
                time_selection.append({'date': day, 'time': time_list})
            elif datetime.now().time() >= time(20, 0, 0):
                # show next three days  basically skip todays day.
                continue
            else:
                #  from current time to and of day
                time_selection.append({'date': day, 'time': time_list[time_list.index(
                    datetime(1, 1, 1, datetime.now().hour, 00, 00))+1:]})
        else:
            #  next 3 days
            time_selection.append({'date': day, 'time': time_list})

    distinct_catagory = Service.objects.order_by().values_list('catagory').distinct()
    filtered_services = []
    for i in distinct_catagory:
        services = Service.objects.filter(catagory=i[0])
        temp = []
        for j in services:
            temp.append(j)
        filtered_services.append({'catagory': i[0], 'services': temp})
    context = {
        'select_time': time_selection,
        'filtered_services': filtered_services,
    }
    return render(request, 'appointment/index.html', context)
