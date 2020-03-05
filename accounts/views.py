from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegistrationForm

class Login(View):
    def get(self, request):
        next = request.GET.get('next')
        form = UserLoginForm()
        context = {
            'form': form,
        }
        return render(request, "login.html", context)

    def post(self, request):
        next = request.GET.get('next')
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect('home')
        return redirect('login')


class Register(View):
    def get(self, request):
        next = request.GET.get('next')
        form = UserRegistrationForm()
        context = {
            'form': form,
        }
        return render(request, "register.html", context)

    def post(self, request):
        next = request.GET.get('next')
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            print("inside registration")
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, user)
            if next:
                return redirect(next)
            return redirect('home')
        return redirect('register')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')
