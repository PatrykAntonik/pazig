from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import *
from .models import *
# Create your views here.

class CreateGroup(LoginRequiredMixin,CreateView):
    fields = ('name','description')
    model = Group
    
class SingleGroup(DetailView):
    model = Group
    
class ListGroups(ListView):
    model = Group
    
class JoinGroup(LoginRequiredMixin,RedirectView):
    model = Group
    
class LeaveGroup(LoginRequiredMixin,RedirectView):
    model = Group
