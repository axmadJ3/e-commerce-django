from django.shortcuts import render


def catalog(request):
    return render(request, template_name='products/catalog.html')


def product(request):
    return render(request, template_name='products/product.html')
 