from django.contrib import admin

from apps.orders.models import Order, OrderItem


class OrderTabular(admin.TabularInline):
    model = Order
    fields = ['requires_delivery', 'status', 'payment_on_get', 'is_paid', 'created_timestamp']
    readonly_fields = ['created_timestamp']
    search_fields = ['requires_delivery', 'status', 'is_paid', 'created_timestamp']
    extra = 0
    
    
class OrderItemTabular(admin.TabularInline):
    model = OrderItem
    fields = ['product', 'name', 'price', 'quantity']
    search_fields = ['product', 'name']
    extra = 0
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'requires_delivery', 'status', 
                    'payment_on_get', 'is_paid', 'created_timestamp'
    ]
    search_fields = ('id',)
    readonly_fields = ['created_timestamp']
    list_filter = ['requires_delivery', 'status', 'payment_on_get', 'is_paid', 'created_timestamp']
    inlines = [OrderItemTabular]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'name', 'price', 'quantity']
    search_fields = ['order', 'product', 'name']
    