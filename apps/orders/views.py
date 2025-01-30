from django.shortcuts import redirect, render
from django.db import transaction
from django.forms import ValidationError
from django.contrib import messages

from .forms import CreateOrderForm
from .models import Order, OrderItem
from apps.carts.models import Cart

def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)
                    
                    if cart_items.exists():
                        # создать заказ
                        order = Order.objects.create(
                            user = user,
                            phone_number = form.cleaned_data['phone_number'],
                            requires_delivery = form.cleaned_data['requires_delivery'],
                            delivery_address = form.cleaned_data['delivery_address'],
                            payment_on_get = form.cleaned_data['payment_on_get'],
                        )
                        # создать элементы заказа
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity
                            
                            if product.quantity < quantity:
                                raise ValidationError(f'Недостаточно количество товара {name} на складе\
                                    В наличии - {product.quantity}')
                                
                            OrderItem.objects.create(
                                order = order,
                                product = product,
                                name = name,
                                price = price,
                                quantity = quantity,
                            )
                            product.quantity -= quantity
                            product.save()
                        
                        # очистить корзину
                        cart_items.delete()
                        
                        messages.success(request, 'Заказ успешно оформлен!')
                        return redirect('user:profile')
            
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('orders:create-order')
        
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)
    
    context = {
        'title': 'HOME - Оформление заказа',
        'form': form,
    }
    return render(request, 'orders/create_order.html', context=context)
