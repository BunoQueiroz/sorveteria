from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from products.models import Product
from .models import User

def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username

        products = Product.objects.all()
        user = User.objects.filter(username=username).get()

        data = {
            'products': products,
            'user': user,
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
            username = request.user.username
            user = User.objects.filter(username=username).get()
            data = {
                'products' : products,
                'user': user,
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
        user = get_object_or_404(User, username=request.user.username)
        user.first_name = request.POST.get('firstName')
        user.last_name = request.POST.get('lastName')
        if 'img' in request.FILES:
            user.img = request.FILES.get('img')
        user.save()

        messages.success(request, 'Dados alterados com sucesso')
        return redirect('my_profile')
