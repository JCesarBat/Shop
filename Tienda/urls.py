# -*- coding: utf-8 -*-
from django.urls import path
from Tienda import views


urlpatterns = [  
    path('Tienda/',views.Tienda_views,name="Tienda"),
    
    
]