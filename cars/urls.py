from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CarsCreate.as_view(), name='car_create'),
]