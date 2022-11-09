from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import validate_form, convert_to_dict

def home(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'core/register.html')

    if request.method == 'POST':
        if (validate_form(request)):
            data = convert_to_dict(request)
            user = User.objects.create_user(username=data['username'],first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['password'], is_superuser=False)
            return redirect('login')
        else:
            return redirect('register')
