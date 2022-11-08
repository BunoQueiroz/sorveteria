from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from random import randrange
from .forms import validate_form

def home(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'core/register.html')

    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        username = first_name + str(randrange(1111,9999))
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        data = {
            'username' : username, 
            'first_name' : first_name, 
            'last_name' : last_name, 
            'email' : email, 
            'password' : password, 
            'confirm_password' : confirm_password
        }

        if (validate_form(data)):
            user = User.objects.create_user(username=username,first_name=first_name, last_name=last_name, email=email, password=password, is_superuser=False)
            return redirect('login')
        else:
            return redirect('register')
