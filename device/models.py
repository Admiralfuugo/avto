from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)
    imei = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class History(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=30)
    temperature = models.CharField(max_length=10)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str.format('{} {}', self.height, self.weight)