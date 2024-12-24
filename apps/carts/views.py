from django.shortcuts import render, redirect

from apps.carts.models import Cart
from apps.products.models import Products

def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product).first()
        
        if carts.exists():
            cart.quantity += 1
            cart.save()
    else:
        cart = Cart.object.create(user=request.user, product=product, quantity=1)
    
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request, product_slug):
    pass

def cart_remove(request, product_slug):
    pass
