from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from .models import Car
from .forms import CarForm


# Create your views here.

class CarsList(ListView):
    template_name = 'cars/list.html'
    model = Car
    fields = '__all__'


class CarsCreate(FormView):
    template_name = 'cars/create.html'
    form_class = CarForm
    fields = '__all__'
    
    def form_valid(self, form):
        form.save()
        return super(CarsCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('car_list')
