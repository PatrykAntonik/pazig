from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreateForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)
    
    class Meta:
        fields = ('username','email','password1','password2','profile_picture')

        model = get_user_model()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['username'].label = 'Nazwa użytkownika'
        # self.fields['email'].label = 'Adres email'