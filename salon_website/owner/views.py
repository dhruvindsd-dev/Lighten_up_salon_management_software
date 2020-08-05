from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Owner, Staff, Salon_token_ids
from appointment.models import Appointment, Client
from notifications.notify_fms import Notify
from home.models import Regi_key
from appointment.models import Appointment, Client, Service
from sales.views import Sale_services
from datetime import datetime, timedelta
from django.db.models import Q


# Create your views here.


def account_verification(request):  # admin login page
    # checks for staff and owner accounts, if exists loges in and checkes for ids, if ids not available then store em , else send password or username invalid.
    if request.POST:
        # print(request.session['gkddlkdfgdfndlk'])
        username = request.POST['username']
        password = request.POST['password']
        token = request.POST['token']
        # create a Salon_token_ids and connect it with the user after retriving it
        if len(Owner.objects.filter(name=username, password=password)) > 0:
            # Owner valid
            request.session['admin_validate'] = True
            owner = Owner.objects.get(
                name=username, password=password)
            if len(Salon_token_ids.objects.filter(token=token)) == 0:
                Salon_token_ids.objects.create(
                    token=token, admin=owner)
            return redirect(f'/staff_loged_in/{username}')
        elif len(Staff.objects.filter(name=username, password=password)) > 0:
            # staff valid
            request.session['admin_validate'] = True
            staff = Staff.objects.get(name=username, password=password)
            if len(Salon_token_ids.objects.filter(token=token)) == 0:
                Salon_token_ids.objects.create(
                    token=token, staff=staff)
        else:
            #  password or username invalid
            return render(request, 'owner/staff_login.html', {'err': 'Invalid Username or password'})
    return render(request, 'owner/staff_login.html')


def not_logged_in(request):
    return render(request, 'owner/not_logged_in.html')


def account_verified(request, username):
    if 'admin_validate' in request.session:
        today = datetime.today().strftime('%Y-%m-%d')
        today_5 = datetime.today() + timedelta(days=5)
        today_5_str = today_5.strftime('%Y-%m-%d')
        anni_cli = Client.objects.filter(
            anniversery__range=[today, today_5_str])
        birth_cli = Client.objects.filter(
            date_of_birth__range=[today, today_5])
        upcomming_events = []
        for cli in birth_cli:
            upcomming_events.append({
                'cli': cli,
                'event': 'birthday',
                'days_to_go': (cli.date_of_birth.day - datetime.today().day)})
        for cli in anni_cli:
            upcomming_events.append(
                {'cli': cli,
                 'event': 'anniversery',
                 'days_to_go': (cli.anniversery.day - datetime.today().day)})
        print(upcomming_events)
        return render(request, 'owner/index.html', {'name': username, 'upcomming_events': upcomming_events})
    else:
        return redirect('/not_logged_in')


def appointment_handle(request):  # rendering all the pending and confirm appointments
    if 'admin_validate' in request.session:
        appointments = Appointment.objects.filter(
            date__gte=datetime.today().strftime('%Y-%m-%d'))
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
    else:
        return redirect('/not_logged_in')


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

#  SERVICES


def services_index(request):
    if 'admin_validate' in request.session:
        context = {
            'services': Service.objects.all()
        }
        return render(request, 'owner/services_index.html', context)
    else:
        return redirect('/not_logged_in')


def create_services(request):
    if 'admin_validate' in request.session:
        if request.POST:
            Service.objects.create(
                name=request.POST['service_name'],
                price=request.POST['service_price'],
                catagory=request.POST['service_catagory'],
                time_taken=request.POST['service_time']
            )
            if request.POST['show_same'] == 'false':
                return redirect('/salon_services')
        return render(request, 'owner/create_services.html')
    else:
        return redirect('/not_logged_in')


def edit_services(request):
    if 'admin_validate' in request.session:
        return render(request, 'owner/create_services.html', {})
    else:
        return redirect('/not_logged_in')

# def delete_services(request):
    # return render(request)

#  CLIENT MANAGEMENT


def admin_client_index(request):
    if 'admin_validate' in request.session:
        clients = Client.objects.all()
        cli_list = []
        # range of 2 months...
        today = datetime.today().date()
        two_months_back = today - timedelta(days=65)
        services_in_range = Sale_services.objects.filter(
            date__range=[two_months_back, today])
        active_clients = 0
        for client in clients:
            active = False
            if len(services_in_range.filter(cli=client)) >= 2:
                active_clients = active_clients + 1
                active = True
            cli_list.append({'cli': client,
                             'type_cli': active,
                             'visits': len(Sale_services.objects.filter(cli=client))})
        #  if a client is comming at least once a month from last 2 months then
        #  if the client is not visiting at least 2 in two months ie 60 days then declare him as  inactive
        return render(request, 'owner/client_index.html', {'clients': cli_list, 'active_cli': active_clients, 'total_cli': clients.count(), 'inactive_cli': (clients.count() - active_clients)})
    else:
        return redirect('/not_logged_in')


def admin_client_view(request, id):
    if 'admin_validate' in request.session:
        cli = Client.objects.get(id=id)
        sale = Sale_services.objects.filter(cli=cli)
        total_visits = sale.count()
        total_sales = 0
        for i in sale:
            total_sales = total_sales + \
                ((i.true_price - (i.true_price*i.discount)/100))
        # active / inacive
        today = datetime.today().date()
        two_months_back = today - timedelta(days=65)
        services_in_range = Sale_services.objects.filter(
            date__range=[two_months_back, today], cli=cli)
        if len(services_in_range) >= 2:
            active = True
        else:
            active = False
        return render(request, 'owner/client_view.html', {'cli': cli, 'type': active, 'sales': total_sales, 'visits': total_visits})
    else:
        return redirect('/not_logged_in')


def admin_client_edit(request, id):
    if 'admin_validate' in request.session:
        if request.POST:
            cli = Client.objects.get(id=id)
            cli.name = request.POST['cli_name']
            cli.number = request.POST['cli_number']
            dt = datetime.strptime(
                request.POST['cli_anniversery'], "%d-%b-%Y")
            cli.anniversery = dt.date()
            dt = datetime.strptime(
                request.POST['cli_dob'], "%d-%b-%Y")
            cli.dob = dt
            cli.save()
            return redirect('/salon_clients')
        return render(request, 'owner/client_edit.html', {'cli': Client.objects.get(id=id)})
    else:
        return redirect('/not_logged_in')
