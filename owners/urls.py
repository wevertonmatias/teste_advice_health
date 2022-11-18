from django.urls import path
from .views import *
urlpatterns = [
    path('', Owners.as_view(), name='owner_list'),
]