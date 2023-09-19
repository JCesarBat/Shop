# -*- coding: utf-8 -*-
from django.urls import path

from ProyectoWebBlog import views      

                      


urlpatterns = [  
    path('blog/',views.blog_name,name="blog"), 
    path('blog/categoria/<int:categoria_id>/',views.categoria_name,name="categoria"),
    
]


