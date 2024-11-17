from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from .forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm()
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)       
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
        
    context = {
        'title': 'HOME - Авторизация',
        'form': form,
    }
    
    return render(request, template_name='users/login.html', context=context)


def registration(request):
    context = {
        
    }
    
    return render(request, template_name='users/registration.html', context=context)


def profile(request):
    context = {
        
    }
    
    return render(request, template_name='users/profile.html', context=context)


def logout(request):
    context = {
        
    }
    
    return render(request, template_name='users/login.html', context=context)
