from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Products
from .utils import query_search


class CatalogView(ListView):
    model = Products
    # queryset = Products.objects.all()
    template_name = 'products/catalog.html'
    context_object_name = 'products'
    paginate_by = 6
    allow_empty = True
    
    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        on_sale = self.request.GET.get('on_sale')
        order_by = self.request.GET.get('order_by')
        query = self.request.GET.get('q')
        
        if category_slug == 'all':
            products = super().get_queryset()
        elif query:
            products = query_search(query)
        else:
            products = super().get_queryset().filter(category__slug=category_slug)
            if not products.exists():
                raise Http404()

        if on_sale:
            products = products.filter(discount__gt=0)
        if order_by and order_by != 'default':
            products = products.order_by(order_by)
            
        return products
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home - Каталог'
        context['category_slug'] = self.kwargs.get('category_slug')
        return context


class ProductView(DetailView):
    # model = Products
    # slug_field = 'slug'
    template_name = 'products/product.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    
    def get_object(self, queryset=None):
        product = Products.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context


# def catalog(request, category_slug=None):
#     on_sale = request.GET.get('on_sale', None)
#     order_by = request.GET.get('order_by', None)
#     query = request.GET.get('q', None)
    
#     if category_slug == 'all':
#         products = Products.objects.all()
#     elif query:
#         products = query_search(query)
#     else:
#         products = Products.objects.filter(category__slug=category_slug)
        
#         if not products.exists():
#             raise Http404()

#     if on_sale:
#         products = products.filter(discount__gt=0)
#     if order_by and order_by != 'default':
#         products = products.order_by(order_by)
    
#     paginator = Paginator(products, 6)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)  
    
#     context = {
#         'title': 'Home - Каталог',
#         'products': page_obj,
#         'category_slug': category_slug,
#     }
    
#     return render(request, template_name='products/catalog.html', context=context)


# def product(request, product_slug):
#     product = get_object_or_404(Products, slug=product_slug)
    
#     context = {
#         'product': product,
#     }
    
#     return render(request, template_name='products/product.html', context=context)
 