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


urlpatterns = [
    path('', include('pwa.urls')),
    path('admin/', admin.site.urls),
    path('', index),
    path('firebase-messaging-sw.js',
         ServiceWorkerView.as_view(), name='service_worker'),
    # path('offline-sw.js',
    #      Offline_ServiceWorkerView.as_view(), name='service_worker'),
    path('notification_token_csrf/<str:token>', notification_token_regi),
    # appointment urls
    path('book_appointment', appointment_index),
    # admin and owner urls
    path('staff-login', account_verification),
    path('staff-logged-in', account_verification),
    path('owner-appointment', appointment_handle),
    path('booking/<str:name>/<int:number>/confirm', appointment_confirm),
    path('booking/<str:name>/<int:number>/decline', appointment_decline),


]
