from django.urls import path

from apps.orders import views

app_name = "orders"

urlpatterns = [
    path('create/', views.CreateOrderView.as_view(), name='create-order'),
]
