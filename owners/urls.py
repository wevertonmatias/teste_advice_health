from django.urls import path
from .views import *
urlpatterns = [
    path('list/', Owners.as_view(), name='owner_list'),
    path('create/', OwnersCreate.as_view(), name='owner_create'),
]