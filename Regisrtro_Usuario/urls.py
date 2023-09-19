# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:42:36 2023

@author: JC
"""

from django.urls import path


from Regisrtro_Usuario import views 


urlpatterns = [ 
    path('Registro/',views.VRegistro.as_view(),name="Registro"),
    path('Logout/',views.cerrar_session,name='Logout'),
    path('logear/',views.logear,name='logear'),
    
    ]
