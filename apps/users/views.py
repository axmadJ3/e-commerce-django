from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm, ProfileChangeForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, Вы вошли в аккаунт!')     
                
                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserLoginForm()
        
    context = {
        'title': 'HOME - Авторизация',
        'form': form,
    }
    
    return render(request, template_name='users/login.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username}, Вы успешно зарегистрировались и вошли в аккаунт!')     
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'HOME - Регистрация',
        'form': form,
    }
    
    return render(request, template_name='users/registration.html', context=context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileChangeForm(data=request.POST, instance=request.user, files=request.FILES )
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен!') 
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileChangeForm(instance=request.user)
    
    context = {
        'title': 'HOME - Кабинет',
        'form': form,
    }
    
    return render(request, template_name='users/profile.html', context=context)


@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, Вы вышли из аккаунта!')
    auth.logout(request)
    return redirect(reverse('main:home'))


def users_cart(request):
    return render(request, template_name='users/users_cart.html')
