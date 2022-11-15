from django.shortcuts import render, redirect
from django.contrib import auth, messages
from products.models import Product
from .models import User
from django.conf import settings
from PIL import Image
from datetime import date
import os

def dashboard(request):
    if request.user.is_authenticated:
        products = Product.objects.all()

        data = {
            'products': products
        }

        return render(request, 'user/dashboard.html', data)
    else:
        return redirect('home')

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso')
    return redirect('home')
    
def search(request):
    if 'search' in request.GET:
        name = request.GET.get('search')
        products = Product.objects.filter(name__icontains=name)
        if products.exists():
            data = {
                'products' : products
            }
            return render(request, 'user/dashboard.html', data)
        messages.error(request, f'Infelizmente ainda não temos {str(name).upper()} em nossa sorveteria')
        return redirect('dashboard')

def my_profile(request):
    if request.user.is_authenticated and request.method == 'GET':
        username = request.user.username

        user = User.objects.filter(username=username).get()

        data = {
            'user': user
        }
        return render(request, 'user/my_profile.html', data)

    elif request.user.is_authenticated and request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        img = request.FILES.get('img')
        username = request.user.username

        img_file = Image.open(img)
        path = os.path.join(settings.BASE_DIR, f'media/users/imgs/{img}')
        img_file.save(path)

        user = User.objects.filter(username=username)
        user.update(first_name=first_name, last_name=last_name, img=path)

        messages.success(request, 'Dados alterados com sucesso')
        return redirect('my_profile')
