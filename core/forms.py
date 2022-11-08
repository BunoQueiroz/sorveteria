from django.contrib.auth.models import User

def validate_form(data_dict):
    return validate_password(data_dict) and email_validate(data_dict) and data_not_empty(data_dict)

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
