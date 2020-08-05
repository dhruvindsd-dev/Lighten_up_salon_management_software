from django.shortcuts import render, redirect
from .models import Sale_services
from appointment.models import Client, Service
from django.db.models import Sum
from datetime import date, datetime
# Create your views here.


def sales_index(request):
    # Service.objects.order_by().values_list('catagory').distinct()
    dates = Sale_services.objects.values_list('date').distinct()
    sale = Sale_services.objects.order_by('-id').all()
    temp = []
    for i in dates:
        sale_obj = sale.filter(date=i[0])
        final_dis_price = 0
        for j in sale_obj:
            final_dis_price = final_dis_price + round(
                j.true_price - ((j.true_price * j.discount)/100), 1)
        temp.append({'sale': sale_obj, 'dis_price': final_dis_price})
    return render(request, 'owner/sales_index.html', {'sales': temp})

# retrive the sales index of the data ....
# check for the date of today ... if not available then create a new modal and then proceed ,
#  get a new sales obj , create a new sales_services obj and relate it to sales obj retrived previously save it finally ...


def add_sales(request):
    if request.POST:
        if request.POST['old_client_num'] == '':
            cli = Client.objects.create(
                name=request.POST['new_client_name'],
                number=request.POST['new_client_number'],
                anniversery=request.POST['cli_anniversery'],
                date_of_birth=request.POST['cli_dob'])
        else:
            cli = Client.objects.get(number=request.POST['old_client_num'])
        if request.POST['discount'] == '':
            discount = 0
        else:
            discount = request.POST['discount']
        sale = Sale_services.objects.create(
            cli=cli,
            services=request.POST['selected_ser'],
            true_price=request.POST['og_price'],
            discount=discount,
            date=datetime.today().date())
        return redirect(f'/sale_view/{sale.date}')
    distinct_catagory = Service.objects.order_by().values_list('catagory').distinct()
    filtered_services = []
    for i in distinct_catagory:
        services = Service.objects.filter(catagory=i[0])
        temp = []
        for j in services:
            temp.append(j)
        filtered_services.append({'catagory': i[0], 'services': temp})
    context = {
        'filtered_services': filtered_services,
        'autosearch_clients': Client.objects.all()
    }
    return render(request, 'owner/sales_create.html', context)


def sales_view(request, date):
    sale = Sale_services.objects.filter(date=date).order_by('-id')
    temp = []
    for i in sale:
        dis_price = round(
            i.true_price - ((i.true_price * i.discount) / 100), 2)
        temp.append({'dis_price': dis_price, 'sale': i})
    return render(request, 'owner/sale_view.html', {'sales': temp})


def sale_edit(request, id):
    og_sale = Sale_services.objects.get(id=id)
    if request.POST:
        if request.POST['old_client_num'] == '':
            cli = Client.objects.create(
                name=request.POST['new_client_name'],
                number=request.POST['new_client_number'],
                anniversery=request.POST['cli_anniversery'],
                date_of_birth=request.POST['cli_dob'])
        else:
            cli = Client.objects.get(number=request.POST['old_client_num'])
        if request.POST['discount'] == '':
            discount = 0
        else:
            discount = request.POST['discount']
        og_sale.cli = cli
        og_sale.services = request.POST['selected_ser']
        og_sale.true_price = request.POST['og_price']
        og_sale.discount = request.POST['discount']
        og_sale.save()
        return redirect(f'/sale_view/{og_sale.date}')
    distinct_catagory = Service.objects.order_by().values_list('catagory').distinct()
    filtered_services = []
    for i in distinct_catagory:
        services = Service.objects.filter(catagory=i[0])
        temp = []
        for j in services:
            temp.append(j)
        filtered_services.append({'catagory': i[0], 'services': temp})
    context = {
        'filtered_services': filtered_services,
        'autosearch_clients': Client.objects.all(),
        'og_sale': og_sale
    }
    return render(request, 'owner/sales_create.html', context)
