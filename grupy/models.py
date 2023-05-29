import markdown
from django import template
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

User = get_user_model()
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    members = models.ManyToManyField(User, through='GroupMember')
    
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = markdown.markdown(self.description)
        super().save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse("grupy:single", kwargs={"slug": self.slug})
        
    class Meta:
        ordering = ['name']
    
    

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)
    
    def __str__(self):
        self.user.username
        
    class Meta:
        unique_together = ('group','user')