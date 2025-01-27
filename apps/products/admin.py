from django.contrib import admin

from .models import Products, Categories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['discount', ]
    search_fields = ['name', 'description']
    list_filter = ['discount', 'price', 'category']
    prepopulated_fields = {'slug': ('name', )}
    fields = [
        'name',
        'category',
        'slug',
        'description',
        'image',
        ('price', 'discount'),
        'quantity',
    ]
    