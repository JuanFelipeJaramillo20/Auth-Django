from django.urls import path
from . import views
from .decorators import admin_only

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signing', views.signing, name="signing"),
    path('signout', views.signout, name="signout"),
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/<int:pk>/update/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('admin/dashboard/', admin_only(views.admin_dashboard), name='admin_dashboard'),
]
