from django.shortcuts import render
from .models import Product


def details_product(request, slug):
    products = Product.objects.filter(slug=slug)
    context = {'products': products}
    return render(request, 'store/product.html', context=context)

