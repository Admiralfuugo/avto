from django.shortcuts import render
from .models import Device, History

def getHistory(request):
    if request.method == "GET":
        imei = request.get['imei']
        device = Device.objects.get(imei)
        