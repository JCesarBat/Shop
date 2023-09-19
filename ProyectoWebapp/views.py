from django.shortcuts import render,redirect
    
# Create your views here.
    
def Home (request):
        
    diccionario={"llave":"Esta es la pagina de Inicio"}
            
    
    return render(request,'ProyectoWebapp/Plantillas/home.html',diccionario)
    
    




