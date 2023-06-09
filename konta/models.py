from django.db import models
from django.contrib import auth
# Create your models here.


class UserModel(auth.models.User, auth.models.PermissionsMixin):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.username
