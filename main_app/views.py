from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
# from .models import Dog
# from django.views.generic.edit import CreateView
# from django.views.generic import DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"



