from django.urls import path, include
from .views import getHistory

urlpatterns = [
    path('', getHistory, name='get-history'),
    
]
