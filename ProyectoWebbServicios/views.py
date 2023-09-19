from django.shortcuts import render
from ProyectoWebbServicios.models import Servicos
def Servicios (request):
    
    todos_Servicios=Servicos.objects.all()
    
    
    
    diccionario={"llave":"Esta es la pagina de Servicios",'servicios':todos_Servicios}
    
    return render(request,'ProyectoWebbServicios/Plantillas/Servicios.html',diccionario)