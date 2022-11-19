from django.urls import path
from .views import *

urlpatterns = [
    path('list/', CarsList.as_view(), name='car_list'),
    path('create/', CarsCreate.as_view(), name='car_create'),
]