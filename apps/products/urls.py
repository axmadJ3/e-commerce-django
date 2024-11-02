from django.urls import path

from . import views


app_name = 'product'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<slug:category_slug>/', views.catalog, name='catalog-detail'),
    path('product/<slug:product_slug>/', views.product, name='product-detail'),
]
