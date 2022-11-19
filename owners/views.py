from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from .models import Owner

class Owners(TemplateView):
    template_name = 'list.html'


class OwnersCreate(CreateView):
    template_name = 'create.html'
    model = Owner
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('owner_list')