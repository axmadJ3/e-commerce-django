from django.shortcuts import redirect
from django.db import transaction
from django.forms import ValidationError
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.orders.forms import CreateOrderForm
from apps.orders.models import Order, OrderItem
from apps.carts.models import Cart


class CreateOrderView(LoginRequiredMixin, FormView):
    template_name = 'orders/create_order.html'
    form_class = CreateOrderForm
    success_url = reverse_lazy('user:profile')
    
    def get_initial(self):
        initial = super().get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        return initial
    
    def form_valid(self, form):
        try:
            with transaction.atomic():
                user = self.request.user
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
                            messages.error(self.request, f'Недостаточно товара {name} на складе. В наличии - {product.quantity}')
                            return redirect('orders:create-order')
                            
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
                    messages.success(self.request, 'Заказ успешно оформлен!')
                    return redirect('user:profile')
        
        except ValidationError as e:
            messages.error(self.request, str(e))
            return redirect('orders:create-order')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка в форме')
        return redirect('orders:create-order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'HOME - Оформление заказа'
        context['order'] = True
        return context
    

# @login_required
# def create_order(request):
#     if request.method == 'POST':
#         form = CreateOrderForm(data=request.POST)
#         if form.is_valid():
#             try:
#                 with transaction.atomic():
#                     user = request.user
#                     cart_items = Cart.objects.filter(user=user)
                    
#                     if cart_items.exists():
#                         # создать заказ
#                         order = Order.objects.create(
#                             user = user,
#                             phone_number = form.cleaned_data['phone_number'],
#                             requires_delivery = form.cleaned_data['requires_delivery'],
#                             delivery_address = form.cleaned_data['delivery_address'],
#                             payment_on_get = form.cleaned_data['payment_on_get'],
#                         )
#                         # создать элементы заказа
#                         for cart_item in cart_items:
#                             product = cart_item.product
#                             name = cart_item.product.name
#                             price = cart_item.product.sell_price()
#                             quantity = cart_item.quantity
                            
#                             if product.quantity < quantity:
#                                 raise ValidationError(f'Недостаточно количество товара {name} на складе\
#                                     В наличии - {product.quantity}')
                                
#                             OrderItem.objects.create(
#                                 order = order,
#                                 product = product,
#                                 name = name,
#                                 price = price,
#                                 quantity = quantity,
#                             )
#                             product.quantity -= quantity
#                             product.save()
                        
#                         # очистить корзину
#                         cart_items.delete()
                        
#                         messages.success(request, 'Заказ успешно оформлен!')
#                         return redirect('user:profile')
            
#             except ValidationError as e:
#                 messages.error(request, str(e))
#                 return redirect('orders:create-order')
        
#     else:
#         initial = {
#             'first_name': request.user.first_name,
#             'last_name': request.user.last_name,
#         }
#         form = CreateOrderForm(initial=initial)
    
#     context = {
#         'title': 'HOME - Оформление заказа',
#         'form': form,
#         'order': True,
#     }
#     return render(request, 'orders/create_order.html', context=context)
