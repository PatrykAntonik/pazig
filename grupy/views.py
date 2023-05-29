from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, RedirectView
from .models import Group, GroupMember

class CreateGroup(LoginRequiredMixin, CreateView):
    fields = ('name', 'description')
    model = Group

class SingleGroup(DetailView):
    model = Group

class ListGroups(ListView):
    model = Group
    context_object_name = 'groups'

class JoinGroup(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('grupy:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except:
            messages.warning(self.request, 'Already a member of this group')
        else:
            messages.success(self.request, "You've joined this group")
        return super().get(request, *args, **kwargs)

class LeaveGroup(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('grupy:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        try:
            membership = GroupMember.objects.get(user=self.request.user, group__slug=self.kwargs.get('slug'))
            membership.delete()
            messages.success(self.request, "You've left this group")
        except GroupMember.DoesNotExist:
            messages.warning(self.request, 'You are not in this group')
        return super().get(request, *args, **kwargs)
