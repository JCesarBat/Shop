# -*- coding: utf-8 -*-

from django.urls import path


from ProyectoWebbServicios import views 


urlpatterns = [ 
    path('Servicios/',views.Servicios,name="Servicios"),
    ]

