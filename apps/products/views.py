from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Products


def catalog(request, category_slug):
    if category_slug == 'all':
        products = Products.objects.all()
    else:
        products = Products.objects.filter(category__slug=category_slug)

    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'title': 'Home - Каталог',
        'products': page_obj,
    }
    
    return render(request, template_name='products/catalog.html', context=context)


def product(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    
    context = {
        'product': product,
    }
    
    return render(request, template_name='products/product.html', context=context)
 