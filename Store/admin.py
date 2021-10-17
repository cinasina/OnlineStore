from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-created',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug',)
    list_filter = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price', 'available',)
    list_editable = ('name', 'price', 'available',)
    search_fields = ('category', 'name', 'slug',)
    list_filter = ('category', 'name', 'available',)
