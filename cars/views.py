from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Car


# Create your views here.
class CarsCreate(CreateView):
    template_name = 'create.html'
    model = Car
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('car_create')

