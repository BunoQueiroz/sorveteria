from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from products.models import Product

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
        print(products)
        if products.exists():
            data = {
                'products' : products
            }
            return render(request, 'user/dashboard.html', data)
        messages.error(request, f'Infelizmente ainda não temos {str(name).upper()} em nossa sorveteria')
        return redirect('dashboard')
