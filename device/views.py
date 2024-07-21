from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Device, History


def getDevices(request):
    devices = Device.objects.all()
    return render(request, 'show-device.html', {'data': devices}) 

def putHistory(request):
    if request.method == "GET":
        imei = request.GET['imei']
        name = request.GET['name']
        location = request.GET['location']
        height = request.GET['height']
        weight = request.GET['weight']
        temp = request.GET['temperature']
        device = Device.objects.filter(imei=imei).first()
        if device is None:
            device = Device.objects.create(imei=imei, name=name, location=location)
            device.save()
        history = History.objects.create(device=device)
        history.height = height
        history.weight = weight
        history.temperature = temp
        history.save()
        return HttpResponse('Message success!')
    return HttpResponse('Message incompletely!')

def getHistory(request, pk):
    device = Device.objects.get(pk=pk)
    hist = History.objects.filter(device=device)
    return render(request, 'show-data.html', {'data': hist})