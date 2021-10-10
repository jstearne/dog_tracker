from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Dog
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'type', 'img', 'good_dog']
    template_name = "dog_create.html"
    success_url = "/"


class DogUpdate(UpdateView):
    model = Dog
    fields = ['name', 'type', 'img', 'good_dog']
    template_name = "dog_update.html"
    success_url = "/dogs/"


class DogDelete(DeleteView):
    model = Dog
    fields = ['name', 'type', 'img', 'good_dog']
    template_name = "dog_delete_confirmation.html"
    success_url = "/dogs/"


class DogList(TemplateView):
    template_name = "dog_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None:
            context["dogs"] = Dog.objects.filter(name__icontains=name) 
            context["header"] = f"Searching for \"{name}\"" 
        else:
            context["dogs"] = Dog.objects.all()
            context["header"] = "Dogs!"
        return context


class DogDetail(DetailView):
    model = Dog
    template_name = "dog_detail.html"



class ContactUs(TemplateView):
    template_name = "contact_us.html"


