from django.shortcuts import render, redirect
from user.models import User
from django.contrib import auth
from .forms import validate_form, convert_to_dict, messages_error, validate_password, email_validate, data_not_empty, login_empty
from django.contrib import messages

def home(request):
    return render(request, 'core/index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'core/login.html')
    
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = [email, password]

        if login_empty(data) or not User.objects.filter(email=email).exists():
            messages.error(request, 'Algo deu errado, por favor tente novamente daqui a alguns minutos')
            return redirect('login')
        
        else:
            name = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=name, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('dashboard')
            messages.error(request, 'Senha incorreta')
            return redirect(login)

def register(request):
    if request.method == 'GET':
        return render(request, 'core/register.html')

    elif request.method == 'POST':
        if (validate_form(request)):
            data = convert_to_dict(request)
            user = User.objects.create_user(username=data['username'],first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['password'], is_superuser=False)
            messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('login')
        else:
            data = convert_to_dict(request)
            if not email_validate(data):
                message_email = 'O email informado ja foi cadastrado no sistema'
                messages.error(request, message_email)

            if not validate_password(data):
                message_password = 'Sua senha estava muito fraca ou a confirmação estava incorreta'
                messages.error(request, message_password)

            if not data_not_empty(data):
                message_empty = 'Não podem haver campos em branco'
                messages.error(request, message_empty)
                
            return redirect('register')
