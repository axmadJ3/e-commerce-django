from django.shortcuts import render, redirect

from apps.carts.models import Cart
from apps.products.models import Products

def cart_add(request, product_slug):
    try:
        product = Products.objects.get(slug=product_slug)
    except Products.DoesNotExist:
        return redirect(request.META['HTTP_REFERER'])
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    pass

def cart_remove(request, product_slug):
    pass
