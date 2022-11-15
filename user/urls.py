from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('search', views.search, name='search'),
    path('my_profile', views.my_profile, name='my_profile'),
]
