from django.forms import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from apps.users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        