from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Device, History

def getHistory(request):
    
    if request.method == "GET":
        imei = request.GET['imei']
        device = Device.objects.get(imei=imei)
        print (device)
        return HttpResponse('Message success!')
    return HttpResponse('Message incompletely!')