# -*- coding: utf-8 -*-

from django.urls import path


from ProyectoWebContacto import views 


urlpatterns = [ 
    path('Contacto/',views.Contactos_vista,name="Contacto"),
    ]
