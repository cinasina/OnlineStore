from django.shortcuts import render, redirect
from .forms import ContactForm, NewsLetterForm
from django.contrib import messages
from Store.models import Category, Product
from Search.forms import SearchForm
from django.db.models import Q


def home(request):
    categories = Category.objects.filter(is_subname=False)
    products = Product.objects.filter(available=True)
    form = SearchForm()
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data['search']
            products = products.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    context = {'products': products, 'categories': categories, 'form': form}
    return render(request, 'home/home.html', context=context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank You! Your Message Has Been Sent', extra_tags='success')
            return redirect('home:home')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})


def news_letters(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = NewsLetterForm()
    return render(request, 'home/home.html', {'form': form})


def tags(request, name):
    products = Product.objects.filter(tags__in=name)
    context = {'products': products}
    return render(request, 'store/brand_product.html', context=context)


def coming_soon(request):
    return render(request, 'home/coming_soon.html')


def about(request):
    return render(request, 'home/about.html')