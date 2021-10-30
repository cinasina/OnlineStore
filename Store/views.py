from django.shortcuts import render
from .models import Product, Category


def product_category(request, name):
    categories = Category.objects.filter(is_subname=True, main_name__name__contains=name)
    products = Product.objects.filter(main_category__name__contains=name)
    context = {'categories': categories, 'products': products}
    return render(request, 'store/category_product.html', context=context)


def product_brands(request, name, slug):
    categories = Category.objects.filter(is_subname=True, main_name__name__contains=name)
    products = Product.objects.filter(sub_category__slug=slug)
    context = {'categories': categories, 'products': products}
    return render(request, 'store/brand_product.html', context=context)


def product_single(request, name, slug, pk):
    products = Product.objects.filter(main_category__name__contains=name, sub_category__slug=slug, pk=pk)
    context = {'products': products}
    return render(request, 'store/product.html', context=context)

