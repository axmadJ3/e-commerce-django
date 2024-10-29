from django.shortcuts import render

from apps.products.models import Categories

def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'HOME - Главная',
        'categories': categories,
    }
    
    return render(request, template_name='main\index.html', context=context)


def about(request):
    context = {
        'title': 'HOME - О нас',
        'text_on_page': 'И о том почему этот магазин класный и т.д.'
    }
    
    return render(request, template_name='main\\about.html', context=context)
