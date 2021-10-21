from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('<slug:slug>/', views.details_product, name='product'),
]
