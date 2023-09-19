from django.shortcuts import render,redirect
from ProyectoWebContacto.forms import FormularioC
from ProyectoWebContacto.models import GuardarInfo   
from django.http import HttpResponse
# Create your views here.

def Contactos_vista(request):

    formulario1=FormularioC(request.POST)
   
    
    diccionario={'llave':'Contacto','formulario':formulario1}
    
    if request.method=='POST' :
        
        
        return redirect('/Contacto/?valido')
        
    

    return render(request,'ProyectoWebContacto/Plantillas/Contacto.html',diccionario)
