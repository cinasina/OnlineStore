from django.urls import path, re_path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('letter/', views.news_letters, name='news_letter'),
    path('tag/<str:name>/', views.tags, name='product_tags'),

]
