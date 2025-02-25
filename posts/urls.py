from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/profile/', views.custom_login_redirect, name='custom_login_redirect'),  # Custom redirect
]