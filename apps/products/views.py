from django.shortcuts import render

from .models import Products


def catalog(request):
    products = Products.objects.all()
    
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
 