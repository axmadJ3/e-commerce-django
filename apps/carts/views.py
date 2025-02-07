from django.http import JsonResponse
from django.views import View

from apps.carts.models import Cart
from apps.products.models import Products
from apps.carts.mixins import CartMixin

class CartAddView(CartMixin, View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        product = Products.objects.get(id=product_id)

        cart = self.get_cart(request, product=product)
        if cart:
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(user=request.user if request.user.is_authenticated else None, 
                                session_key=request.session.session_key if not request.user.is_authenticated else None,
                                product=product, quantity=1)
        
        response_data = {
            'message': 'Товар успешно добавлен в корзину',
            'cart_items_html': self.render_cart_items(request)
        }        

        return JsonResponse(response_data)


class CartChangeView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get('cart_id')
        cart = self.get_cart(request, cart_id=cart_id)
        cart.quantity = request.POST.get('quantity')
        cart.save()
        quantity_deleted = cart.quantity
        
        response_data = {
            'message': 'Количество товара успешно изменено',
            'cart_items_html': self.render_cart_items(request),
            'quantity_deleted': quantity_deleted
        }
        
        return JsonResponse(response_data)


class CartRemoveView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get('cart_id')
        cart = self.get_cart(request, cart_id=cart_id)
        quantity_deleted = cart.quantity
        cart.delete()
        
        response_data = {
            'message': 'Товар успешно удален из корзины',
            'cart_items_html': self.render_cart_items(request),
            'quantity_deleted': quantity_deleted
        }
        
        return JsonResponse(response_data)


# def cart_add(request):
#     product_id = request.POST.get('product_id')
    
#     product = Products.objects.get(id=product_id)

#     if request.user.is_authenticated:
#         carts = Cart.objects.filter(user=request.user, product=product)
        
#         if carts.exists():
#             cart = carts.first()
#             if cart:
#                 cart.quantity += 1
#                 cart.save()
#         else:
#             Cart.objects.create(user=request.user, product=product, quantity=1)
    
#     else:
#         carts = Cart.objects.filter(session_key=request.session.session_key, product=product)
        
#         if carts.exists():
#             cart = carts.first()
#             if cart:
#                 cart.quantity += 1
#                 cart.save()
#         else:
#             Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)
    
#     user_cart = get_user_cart(request)
#     cart_items_html = render_to_string(
#         'carts/includes/included_cart.html', {'carts': user_cart}, request=request)
    
#     response_data = {
#         'message': 'Товар успешно добавлен в корзину',
#         'cart_items_html': cart_items_html,
#     }
    
#     return JsonResponse(response_data)


# def cart_change(request):
#     cart_id = request.POST.get('cart_id')
#     quantity = request.POST.get('quantity')
    
#     cart = Cart.objects.get(id=cart_id)
    
#     cart.quantity = quantity
#     cart.save()
#     updated_quantity = cart.quantity
    
#     user_cart = get_user_cart(request)
#     context = {"carts": user_cart}
#     # if referer page is create_order add key orders: True to context
#     referer = request.META.get('HTTP_REFERER')
#     if reverse('orders:create-order') in referer:
#         context["order"] = True
    
#     cart_items_html = render_to_string(
#         "carts/includes/included_cart.html", context, request=request)
    
#     response_data = {
#         'message': 'Количество товара успешно изменено',
#         'cart_items_html': cart_items_html,
#         'quantity_deleted': updated_quantity,
#     }
    
#     return JsonResponse(response_data)


# def cart_remove(request):
#     cart_id = request.POST.get('cart_id')
    
#     cart = Cart.objects.get(id=cart_id)
#     quantity = cart.quantity
#     cart.delete()
    
#     user_cart = get_user_cart(request)
#     context = {"carts": user_cart}
#     # if referer page is create_order add key orders: True to context
#     referer = request.META.get('HTTP_REFERER')
#     if reverse('orders:create_order') in referer:
#         context["order"] = True
#     cart_items_html = render_to_string(
#         "carts/includes/included_cart.html", context, request=request)
    
#     response_data = {
#         'message': 'Товар успешно удален из корзины',
#         'cart_items_html': cart_items_html,
#         'quantity_deleted': quantity,
#     }
    
#     return JsonResponse(response_data)
