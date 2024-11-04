from django import template
from django.utils.http import urlencode

from apps.products.models import Categories

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def tag_products(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(**kwargs)
    return urlencode(query)