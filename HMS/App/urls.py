from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
     path('' , views.home , name="home") , 
     path('details/<id>/' , views.details , name="details") ,
     path('login/' , views.loginView , name="login") , 
     path('signup/' , views.SignupView , name="signup") ,
     path('logout/' , views.LogoutView , name="logout") 
]
