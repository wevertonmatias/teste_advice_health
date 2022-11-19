from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Owner

class Owners(ListView):
    template_name = 'list.html'
    model = Owner
    fields = '__all__'
    paginate_by = 2


class OwnersCreate(CreateView):
    template_name = 'create.html'
    model = Owner
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('owner_list')

