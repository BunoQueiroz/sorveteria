from django.contrib import admin
from .models import *

class ListProducts(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price')
    list_editable = ('name', 'price')
    list_filter = ('name',)
    list_per_page = 10

class ListCategory(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_editable = ('category',)
    list_per_page = 10

admin.site.register(Product, ListProducts)
admin.site.register(Category, ListCategory)
