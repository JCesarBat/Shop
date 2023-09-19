from django.shortcuts import render
from Tienda.models import Productos
# Create your views here.




def Tienda_views (request):
    
    producto=Productos.objects.all()
    
    diccionario={"llave":"Esta es la Tienda",'Producto':producto}
    
    return render(request,'Tienda/Plantillas/Tienda.html',diccionario)