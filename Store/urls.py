from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('<str:name>/', views.product_category, name='product_category'),
    path('<str:name>/<slug:slug>/', views.product_brands, name='product_brands'),
    path('<str:name>/<slug:slug>/<int:pk>/', views.product_single, name='product_single'),
]
