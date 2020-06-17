from django.shortcuts import render
from django.http import JsonResponse
from .models import Owner, Staff, Salon_token_ids
from appointment.models import Appointment, Client
from notifications.notify_fms import Notify
from home.models import Regi_key
from appointment.models import Appointment, Client
# Create your views here.


def admin_index(request):  # admin home page
    return render(request, 'admin/index.html')


def account_verification(request):  # admin login page
    if request.POST:
        # print(request.session['gkddlkdfgdfndlk'])
        username = request.POST['username']
        password = request.POST['password']
        token = request.POST['token']
        # create a Salon_token_ids and connect it with the user after retriving it
        if len(Owner.objects.filter(name=username, password=password)) > 0:
            request.session['admin_validate'] = True
            # Owner valid
            owner = Owner.objects.get(
                name=username, password=password)
            if len(Salon_token_ids.objects.filter(token=token)) == 0:
                new_token = Salon_token_ids.objects.create(
                    token=token, admin=owner)
            return render(request, 'owner/index.html', {'name': username})
        elif len(Staff.objects.filter(name=username, password=password)) > 0:
            # staff valid
            request.session['admin_validate'] = True
            staff = Staff.objects.get(name=username, password=password)
            if len(Salon_token_ids.objects.filter(token=token)) == 0:
                new_token = Salon_token_ids.objects.create(
                    token=token, staff=staff)
        else:
            #  password or username invalid
            return render(request, 'owner/staff_login.html', {'err': 'Invalid Username or password'})
    return render(request, 'owner/staff_login.html')


def appointment_handle(request):  # rendering all the pending and confirm appointments
    appointments = Appointment.objects.all()
    pending_appointments = []
    confirmed_appointment = []
    for i in appointments:
        if i.confirmation == False:
            services_list = i.work_to_be_done.split(',')
            services_list.pop()
            pending_appointments.append([i, services_list])
        elif i.confirmation == True:
            services_list = i.work_to_be_done.split(',')
            services_list.pop()
            confirmed_appointment.append([i, services_list])
    context = {
        'pending_appointments': pending_appointments,
        'confirmed_appointments': confirmed_appointment,
    }
    return render(request, 'owner/appointment-handle-owner.html', context)


# a sort to api to get name and number of the client and confirm her pending appointment
def appointment_confirm(request, id):
    if 'admin_validate' in request.session:
        appointment = Appointment.objects.filter(id=id)
        if len(appointment) > 0:
            appointment[0].confirmation = True
            appointment[0].save()
            tokens = Regi_key.objects.filter(cli=appointment[0].cli)
            print('[tokens]', tokens)
            if len(tokens) > 0:
                token_list = []
                for i in tokens:
                    token_list.append(i.token)
                notify = Notify(token_list)
                notify.send_cli_confirmation(
                    cli_name=appointment[0].cli.name, cli_date=appointment[0].date, cli_time=appointment[0].time)
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({"status": 'failed'})
    else:
        return JsonResponse({'status': 'authentication_failed'})


def appointment_decline(request, id):
    if 'admin_validate' in request.session:
        Appointment.objects.get(id=id).delete()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'authentication_failed'})
# def ajax_test(request):
    # if request.method == "POST" and request.is_ajax():
    # form = ContactForm(request.POST)
    # form.save()
    # return JsonResponse({"success": True}, status=200)
    # return JsonResponse({"success": False}, status=400)
