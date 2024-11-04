from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Products
from .utils import query_search


def catalog(request, category_slug=None):
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)
    
    if category_slug == 'all':
        products = Products.objects.all()
    elif query:
        products = query_search(query)
    else:
        products = Products.objects.filter(category__slug=category_slug)

    if on_sale:
        products = products.filter(discount__gt=0)
    if order_by and order_by != 'default':
        products = products.order_by(order_by)
    
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    
    context = {
        'title': 'Home - Каталог',
        'products': page_obj,
        'category_slug': category_slug,
    }
    
    return render(request, template_name='products/catalog.html', context=context)


def product(request, product_slug):
    product = get_object_or_404(Products, slug=product_slug)
    
    context = {
        'product': product,
    }
    
    return render(request, template_name='products/product.html', context=context)
 