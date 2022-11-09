from django.contrib.auth.models import User
from random import randrange

def validate_form(request):
    data_dict = convert_to_dict(request)
    return validate_password(data_dict) and email_validate(data_dict) and data_not_empty(data_dict)

def convert_to_dict(request):
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
    return data

def email_validate(data_dict):
    email = data_dict['email']
    if User.objects.filter(email=email).exists():
        return False
    return True    

def data_not_empty(data_dict):
    def remove_blanck(item):
        return str(item).replace(" ", "")

    for _,i in data_dict.items():
        i = remove_blanck(i)
        if i == "":
            return False
    return True

def validate_password(data_dict):
    password = data_dict['password']
    confirm_password = data_dict['confirm_password']
    if password == confirm_password and len(str(password)) >= 8:
        return True
    return False
