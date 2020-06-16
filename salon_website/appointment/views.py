from django.shortcuts import render
from .models import Client, Appointment, Time_slots
from home.models import Regi_key
from notifications.notify_fms import Notify
from owner.models import Salon_token_ids
# Create your views here.


def appointment_index(request):
    if request.POST:
        cli_name = request.POST['cli_name']
        cli_number = request.POST['cli_number']
        cli_services = request.POST['cli_services']
        cli_time = request.POST['cli_time']
        cli_token = request.POST['cli_token']
        print('[CLI_TOKEN]', cli_token)
        temp = cli_time.split('-')
        time = temp[0]
        print(time)
        date = temp[1].split(' ')[1]
        if len(Client.objects.filter(number=cli_number)) == 0:
            # create cli
            Client.objects.create(name=cli_name, number=cli_number)
            cli = Client.objects.get(number=cli_number)
            regi_token = Regi_key.objects.filter(token=cli_token)
            if len(regi_token) == 0:
                Regi_key.objects.create(token=cli_token, cli=cli)
            else:
                regi_token[0].cli = cli
                regi_token[0].save()
        else:
            cli = Client.objects.get(number=cli_number)
            regi_token = Regi_key.objects.filter(token=cli_token)
            if len(regi_token) == 0:
                Regi_key.objects.create(token=cli_token, cli=cli)
            else:
                regi_token[0].cli = cli
                regi_token[0].save()

        Appointment.objects.create(
            time=f'{time}:00', date=f'2020-06-{date}', confirmation=False, work_to_be_done=cli_services, cli=cli)
        tokens = Salon_token_ids.objects.all()
        to_notify_tokens = []
        for token in tokens:
            to_notify_tokens.append(token.token)
        admin_notify = Notify(to_notify_tokens)
        admin_notify.send_admin_prompt(
            cli_name=cli_name, cli_date=temp[1], cli_services=cli_services)

        return render(request, 'appointment/thank-you.html')
        #  get the data and send a notification to the admins and put the appointment on pending.
        # slot timings PENDING
    time = Time_slots.objects.all()
    #  [{date : date, time : []}]
    time_selection = []
    for i in time:
        day = i.date.weekday()
        if day == 0:
            day = 'Mon'
        elif day == 1:
            day = 'Tue'
        elif day == 2:
            day = 'Wed'
        elif day == 3:
            day = 'Thur'
        elif day == 4:
            day = 'Fri'
        elif day == 5:
            day = 'Sat'
        elif day == 6:
            day = 'Sun'
        time_selection.append(
            {'date': i.date.day, 'day': day, 'time': i.time_available.split(',')})
    context = {
        'select_time': time_selection
    }
    return render(request, 'appointment/index.html', context)
