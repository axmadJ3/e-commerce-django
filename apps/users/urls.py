from django.urls import path

from apps.users import views


app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.logout, name='logout'),
    path('users-cart/', views.UserCartView.as_view(), name='users_cart'),
]
 