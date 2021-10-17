from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import User
from django.contrib.auth.decorators import login_required


def user_login(request):
    next_url = request.POST.get('next')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            login(request, user)
            messages.success(request, 'You Login Successfully', extra_tags='success')
            if next_url:
                return redirect(next_url)
            else:
                messages.error(request, 'Your Email Or Password Is Wrong!', extra_tags='error')
            return redirect('accounts:login')
        return redirect('home:home')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = User.objects.create_user(email=email, phone_number=phone_number, password=password)
            user.save()
            login_user = authenticate(request, email=email, password=password)
            login(request, login_user)
            messages.success(request, 'You Login Successfully', extra_tags='success')
            return redirect('home:home')
        else:
            messages.error(request, 'Something Is Wrong!', extra_tags='error')
            return redirect('accounts:register')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'See You Soon', extra_tags='success')
    return redirect('home:home')
