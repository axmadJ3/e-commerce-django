from django.contrib import admin

from .models import Products, Categories

admin.site.register(Categories)
admin.site.register(Products)
