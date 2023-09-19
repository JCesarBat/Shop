# -*- coding: utf-8 -*-
from django import forms


class FormularioRegistro(forms.Form):
    nombre=forms.CharField(label='nombre',required=True)
    passwuord=forms.CharField(label='password',required=True,widget=forms.PasswordInput)
    password_confirm=forms.CharField(label='password_confirm',required=True,widget=forms.PasswordInput)
    email=forms.EmailField(label='email',required=True)
    
    
class FormularioLogin(forms.Form):
     nombre=forms.CharField(label='nombre')
     password=forms.CharField(label='password',widget=forms.PasswordInput)
     

    
    
