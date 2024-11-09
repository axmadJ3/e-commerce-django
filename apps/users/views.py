from django.shortcuts import render


def login(request):
    context = {
        
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
