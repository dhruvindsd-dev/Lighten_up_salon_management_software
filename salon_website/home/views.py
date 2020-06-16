from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Regi_key

# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def notification_token_regi(request, token):  # , token, name, num:
    # HTTP_REFERER
    if 'HTTP_REFERER' in request.META:
        if request.META['HTTP_REFERER'] == 'http://127.0.0.1:8000/':
            if len(Regi_key.objects.filter(token=token)) == 0:
                Regi_key.objects.create(token=token)
    else:
        return JsonResponse({'Status': 'Authorization Failed'})
    return JsonResponse({'Status': 'Success'})


# serving firebase-messaging-sw to the main firebase app.
class ServiceWorkerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/firebase-messaging-sw.js', content_type="application/x-javascript")


# class Offline_ServiceWorkerView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'home/sw-offline.js', content_type="application/x-javascript")
