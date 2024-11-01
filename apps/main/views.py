from django.shortcuts import render

from apps.products.models import Categories

def index(request):
    context = {
        'title': 'HOME - Главная',
    }
    
    return render(request, template_name='main\index.html', context=context)


def about(request):
    context = {
        'title': 'HOME - О нас',
        'text_on_page': 'И о том почему этот магазин класный и т.д.'
    }
    
    return render(request, template_name='main\\about.html', context=context)
