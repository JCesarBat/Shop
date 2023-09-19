from django.shortcuts import render,redirect

from carrito.carro import Carro

from Tienda.models import Productos



# Create your views here.


def agregar_producto(request,producto_id):
    
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    
    if producto.disponibilidad ==False :
      return  redirect('/Tienda/?no_se_encuentra')
   
    carro.agregar(producto)
    
    return redirect('Tienda')


def eliminar_producto(request,producto_id):
    
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    
    carro.eliminar(producto)
    
    return redirect('Tienda')


def restar_producto(request,producto_id):
    
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    
    carro.restar(producto)
    
    return redirect('Tienda')

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar()
    return redirect('Tienda')