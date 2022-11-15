from django.contrib import admin
from .models import User

class ListUsers(admin.ModelAdmin):
    list_display = ('img',)

admin.site.register(User)
