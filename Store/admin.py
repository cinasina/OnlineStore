from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('-created',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'slug',)
    list_filter = ('name',)


@admin.action(description='Make products unavailable')
def make_unavailable(product, request, queryset):
    queryset.update(available=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'price', 'available',)
    list_editable = ('name', 'price', 'available',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('category', 'name', 'slug',)
    list_filter = ('category', 'name', 'available',)
    actions = (make_unavailable,)


