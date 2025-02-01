from django.db import models

from apps.users.models import User
from apps.products.models import Products


class CartQuerySet(models.QuerySet):
    def total_price(self):
        return sum(cart.product_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Товар')
    session_key = models.CharField(max_length=32, blank=True, null=True, verbose_name='Ключ сессии')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    
    
    class Meta:
        db_table = 'carts'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ("id",)
    
    
    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
        
    def __str__(self):
        if self.user:
            return f'Kорзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}'
        return f'Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}'
    
    objects = CartQuerySet().as_manager()
    