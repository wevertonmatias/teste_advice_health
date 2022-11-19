from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Car


# Create your views here.

class CarsList(ListView):
    template_name = 'cars/list.html'
    model = Car
    fields = '__all__'


class CarsCreate(CreateView):
    template_name = 'cars/create.html'
    model = Car
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('car_create')
