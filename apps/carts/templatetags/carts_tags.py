from django import template

from apps.carts.utils import get_user_cart

register = template.Library()

@register.simple_tag()
def user_carts(request):
    return get_user_cart(request)
