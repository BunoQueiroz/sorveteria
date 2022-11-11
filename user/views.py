from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from core import views

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'user/dashboard.html')
    else:
        return redirect(views.home)

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso')
    return redirect(views.home)
    