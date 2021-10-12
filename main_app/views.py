from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Dog
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dog_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


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

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            # context["dogs"] = DogList.objects.all()
            return context

class ContactUs(TemplateView):
    template_name = "contact_us.html"


