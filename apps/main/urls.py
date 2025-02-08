from django.urls import path
from django.views.decorators.cache import cache_page

from apps.main import views


app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about/', cache_page(60) (views.AboutView.as_view()), name='about'),
]
