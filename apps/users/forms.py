from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from .models import User

class UserLoginForm(AuthenticationForm):    
    class Meta:
        model = User
        fields = ['username', 'password']
        
        
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password2 = forms.CharField()
    password1 = forms.CharField()


class ProfileChangeForm(UserChangeForm):
    class Meta:
        model = User    
        fields = (
            'image',
            'first_name',
            'last_name',
            'username',
            'email',
        )
    
    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    