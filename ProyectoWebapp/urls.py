# -*- coding: utf-8 -*-

from django.urls import path

from ProyectoWebapp import views 

urlpatterns = [  
    path('home/',views.Home,name="home"),
    
    
]