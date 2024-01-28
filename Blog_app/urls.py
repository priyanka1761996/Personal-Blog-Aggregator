from django.contrib import admin
from django.urls import path
from Blog_app import views


urlpatterns = [
    path('',views.registerPage, name = 'register'),
    path('login/',views.loginPage, name ='login'),
    path('logout/',views.logoutUser, name ='logout'),
    path('home/',views.home, name = 'home'),
    
]
