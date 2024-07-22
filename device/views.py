from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Device, History
from django.http import JsonResponse

def getDevices(request):
    devices = Device.objects.all()
    return render(request, 'show-device.html', {'data': devices})


def getChartData(request, pk):
    device = Device.objects.get(pk=pk)
    hist = History.objects.filter(device=device)
    labels = []
    height = []
    weight = []
    for h in hist:
        labels.append(h.datetime)
        height.append(h.height)
        weight.append(h.weight)
    return JsonResponse(data={
        'labels': labels,
        'height': height,
        'weight': weight,
    })

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
    return HttpResponse('Only method GET')

def getHistory(request, pk):
    device = Device.objects.get(pk=pk)
    hist = History.objects.filter(device=device)
    return render(request, 'show-data.html', {'device': device.id, 'data': hist})

