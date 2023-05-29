from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import *
from .models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.

class CreateGroup(LoginRequiredMixin,CreateView):
    fields = ('name','description')
    model = Group
    
class SingleGroup(DetailView):
    model = Group
    
class ListGroups(ListView):
    model = Group
    
class JoinGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self,*args, **kwargs):
        return reverse('grupy:single',kwargs={'slug',self.kwargs.get('slug')})
    
    def get(self,request,*args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        
        try:
            GroupMember.objects.create(user = self.request.user, group=group)
            
        except:
            messages.warning(self.request,'Alredy a member of this group')
        
        else: 
            messages.warning(self.request,"You've joined this group")
            
        return super().get(request,*args, **kwargs)
    
class LeaveGroup(LoginRequiredMixin,RedirectView):
        def get_redirect_url(self,*args, **kwargs):
            return reverse('grupy:single',kwargs={'slug',self.kwargs.get('slug')})
        
        def get(self,request,*args, **kwargs):
            group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
            
            try:
                membership = GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug')).get()
                                
            except models.GroupMember.DoesNotExist:
                messages.warning(self.request,'You are not in this group')
                
            else: 
                membership.delete()
                messages.warning(self.request,"You've left this group")
                
            return super().get(request,*args, **kwargs)
