from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from .views import *
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .forms import *
# Create your views here.

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'konta/signup.html'    