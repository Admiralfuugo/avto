from django.urls import path, include
from .views import putHistory, getHistory, getDevices

urlpatterns = [
    path('put/', putHistory, name='put-history'),
    path('get/<pk>', getHistory, name='show-history'),
    path('get/', getDevices, name='show-device'),
    
]
