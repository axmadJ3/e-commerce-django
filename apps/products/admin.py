from django.contrib import admin

from .models import Products, Categories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug']
    
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    prepopulated_fields = {'slug': ('name', )}
    # readonly_fields = ['slug']