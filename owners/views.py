from django.shortcuts import render
from django.views.generic import TemplateView

class Owners(TemplateView):
    template_name = 'list.html'