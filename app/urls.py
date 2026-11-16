from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register.as_view(), name='register'),
    path('products/', views.productapiview.as_view(), name='products'),
    path('products/<int:id>/', views.productsapiview.as_view(), name='product-detail'),
]
