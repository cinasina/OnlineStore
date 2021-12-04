from django.shortcuts import render
from .models import Product, Category
from .forms import QuantityForm


def product_category(request, name):
    categories = Category.objects.filter(is_subname=True, main_name__name__contains=name)
    products = Product.objects.filter(main_category__name__contains=name)
    product_all = Product.objects.all()
    num_cat = {}
    for category in product_all:
        num_cat[category.sub_category] = num_cat.get(category.sub_category, 0) + 1
    context = {'categories': categories, 'products': products, 'num_cat': num_cat}
    return render(request, 'store/category_product.html', context=context)


def product_brands(request, name, slug):
    categories = Category.objects.filter(is_subname=True, main_name__name__contains=name)
    products = Product.objects.filter(sub_category__slug=slug)
    context = {'categories': categories, 'products': products}
    return render(request, 'store/brand_product.html', context=context)


def product_single(request, name, slug, pk):
    products = Product.objects.filter(main_category__name__contains=name, sub_category__slug=slug, pk=pk)
    form = QuantityForm()
    context = {'products': products, 'form': form}
    return render(request, 'store/product.html', context=context)
