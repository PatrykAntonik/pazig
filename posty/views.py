from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse
from braces.views import SelectRelatedMixin
from .models import *
from .forms import *
from django.contrib.auth import get_user_model

User = get_user_model()

class PostList(SelectRelatedMixin,ListView):
    model = models.Post
    select_related = ('user','group')
    
class UserPost(ListView):
    model = models.Post
    template_name = 'posty/user_post_list.html'
    
    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related().get(username__iexact=self.kwargs.get('username'))
            return self.post_user.posts.all()
        except User.DoesNotExist:
            raise Http404
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user 
        return context


class PostDetail(SelectRelatedMixin,DetailView):
    model = models.Post
    select_related = ('user','group')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))
    
    
class CreatePost(LoginRequiredMixin,SelectRelatedMixin,CreateView):
    fields = ('message','group')
    model = models.Post
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        joined_group_ids = GroupMember.objects.filter(user_id=self.request.user.id).values_list('group_id', flat=True)
        form.fields['group'].queryset = Group.objects.filter(id__in=joined_group_ids)
        return form
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    
    
class DeletePost(LoginRequiredMixin,SelectRelatedMixin,DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)
    
    def delete(self,*args, **kwargs):
        messages.success(self.request,'Post deleted')
        return super().delete(*args, **kwargs)
        