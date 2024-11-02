from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Products


def catalog(request, category_slug):
    if category_slug == 'all':
        products = Products.objects.all()
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    
    context = {
        'title': 'Home - Каталог',
        'products': products,
    }
    
    return render(request, template_name='products/catalog.html', context=context)


def product(request, product_slug):
    try:
        product = Products.objects.get(slug=product_slug)
    except Exception as e:
        return e
    
    context = {
        'product': product,
    }
    
    return render(request, template_name='products/product.html', context=context)
 