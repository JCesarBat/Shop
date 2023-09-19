from django.db import models

# Create your models here.


class Categoria_Producto(models.Model) :
        nombre=models.CharField(max_length=55)
        creado=models.DateTimeField(auto_now_add=True)
        actualizado=models.DateTimeField(auto_now_add=True)
        class Meta :
            verbose_name='Categoria Producto'
            verbose_name_plural='Categorias Productos'
        
        def __str__(self):
            return self.nombre



class Productos(models.Model) :
     nombre=models.CharField(max_length=55)
     
     precio=models.FloatField()
     
     disponibilidad=models.BooleanField()
     
     categorias=models.ForeignKey(Categoria_Producto, on_delete=models.CASCADE)
     
     imagen=models.ImageField(upload_to='Tienda')
     
     class Meta :
         verbose_name=' Producto'
         verbose_name_plural=' Productos'
         
     def __str__(self):
          return self.nombre
    
     
    