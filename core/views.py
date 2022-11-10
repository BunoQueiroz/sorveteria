from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import validate_form, convert_to_dict, messages_error, validate_password, email_validate, data_not_empty
from django.contrib import messages

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
            messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('login')
        else:
            data = convert_to_dict(request)
            if not email_validate(data):
                message_email = 'O email informado ja foi cadastrado no sistema'
                messages.error(request, message_email)

            if not validate_password(data):
                print('iih rapaz')
                message_password = 'Sua senha estava muito fraca ou a confirmação estava incorreta'
                messages.error(request, message_password)

            if not data_not_empty(data):
                print('iih rapaz')
                message_empty = 'Não podem haver campos em branco'
                messages.error(request, message_empty)
                
            return redirect('register')
