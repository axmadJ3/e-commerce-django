from django.contrib import admin

from .models import Cart

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = 'product', 'quantity', 'created_timestamp'
    search_fields = 'product', 'quantity', 'created_timestamp'
    readonly_fields = ('created_timestamp', )
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product__name', 'quantity', 'created_timestamp')
    list_filter = ('user', 'product__name', 'created_timestamp')
    