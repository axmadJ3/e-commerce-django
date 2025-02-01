from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Prefetch

from apps.carts.models import Cart
from .forms import UserLoginForm, UserRegistrationForm, ProfileChangeForm
from apps.orders.models import Order, OrderItem


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            
            session_key = request.session.session_key
            
            if user:
                auth.login(request, user)
                messages.success(request, f'{username}, Вы вошли в аккаунт!')  
                
                if session_key:
                    forgot_carts = Cart.objects.filter(user=user)
                    if forgot_carts.exists():
                        forgot_carts.delete()
                        
                    Cart.objects.filter(session_key=session_key).update(user=user)
                
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
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
            
            session_key = request.session.session_key
            
            user = form.instance
            auth.login(request, user)
            
            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
            
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
    
    orders = (
        Order.objects.filter(user=request.user)
        .prefetch_related(
            Prefetch(
                'orderitem_set',
                queryset=OrderItem.objects.select_related('product'),
            )
        ).order_by('-id')
    )
    
    context = {
        'title': 'HOME - Кабинет',
        'form': form,
        'orders': orders,
    }
    
    return render(request, template_name='users/profile.html', context=context)


@login_required
def logout(request):
    messages.success(request, f'{request.user.username}, Вы вышли из аккаунта!')
    auth.logout(request)
    return redirect(reverse('main:home'))


def users_cart(request):
    return render(request, template_name='users/users_cart.html')
