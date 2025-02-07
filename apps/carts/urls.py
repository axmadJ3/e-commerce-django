from django.urls import path
from apps.carts import views

app_name = 'carts'

urlpatterns = [
    path('cart-add/', views.CartAddView.as_view(), name='cart_add'),
    path('cart-change/', views.CartChangeView.as_view(), name='cart_change'),
    path('cart-remove/', views.CartRemoveView.as_view(), name='cart_remove'),
]
