from django.contrib import admin

from .models import User
from apps.carts.admin import CartTabAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    inlines = [CartTabAdmin]
    