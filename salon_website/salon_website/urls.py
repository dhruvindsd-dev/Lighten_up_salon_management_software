"""salon_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import *
from appointment.views import *
from owner.views import *
from blog.views import *
from sales.views import *

urlpatterns = [
    path('', include('pwa.urls')),
    path('admin/', admin.site.urls),
    path('', index),
    path('firebase-messaging-sw.js',
         ServiceWorkerView.as_view(), name='service_worker'),

    path('notification_token_csrf/<str:token>', notification_token_regi),
    # appointment urls

    path('book_appointment', appointment_index),
    # admin and owner urls
    path('staff-login', account_verification),
    path('staff_loged_in/<str:username>', account_verified),
    path('not_logged_in', not_logged_in),
    #  appointment
    path('owner-appointment', appointment_handle),
    path('booking/<int:id>/confirm', appointment_confirm),
    path('booking/<int:id>/decline', appointment_decline),
    # admin blog
    path('salon_blog', blog_admin_index),
    path('salon_blog_view/<int:blog_id>', view_blog),
    path('salon_create_blog', create_blog),
    path('salon_blog_img', img_selection),
    # path('salon_blog_img/<str:img_link>', img_selection),
    path('salon_img_save/<int:id>/<path:img_link>', img_selection),

    # sales
    path('sales', sales_index),
    path('sale_add', add_sales),
    path('sale_view/<str:date>', sales_view),
    path('sale_edit/<str:id>', sale_edit),

    # services
    path('salon_services', services_index),
    path('salon_services/create', create_services),
    path('salon_services/edit', edit_services),
    
    # ADMIN CLIENT HANDLE:
    path("salon_clients", admin_client_index),
    path('salon_clients_view/<int:id>', admin_client_view),
    path('salon_clients_edit/<int:id>', admin_client_edit),

    # upcomming events :
]
