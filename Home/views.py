from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def home(request):
    return render(request, 'home/home.html')


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

