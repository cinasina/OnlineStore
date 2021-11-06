from django.shortcuts import render, redirect, get_object_or_404
from .cart import Cart
from Store.models import Product
from Store.forms import QuantityForm


def cart(request):
    user_cart = Cart(request)
    context = {'cart': user_cart}
    return render(request, 'cart/cart.html', context=context)


def add_product(request, product_id):
    user_cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    form = QuantityForm(request.POST)
    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        user_cart.add_product(product=product, quantity=quantity)
        return redirect('cart:cart_details')


def remove_product(request, product_id):
    user_cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    user_cart.remove_product(product)
    return redirect('cart:cart_details')


