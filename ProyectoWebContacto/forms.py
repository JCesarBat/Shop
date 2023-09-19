# -*- coding: utf-8 -*-

from django import forms

            

class FormularioC(forms.Form):
    nombre=forms.CharField(label='Nombre',required=True)
    
    email=forms.EmailField(label='Email',required=True)
    
    contenido=forms.CharField(label='Contenido',widget=forms.Textarea)
