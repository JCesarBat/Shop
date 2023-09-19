from django.contrib import admin
from  Tienda.models import Categoria_Producto,Productos

# Register your models here.
class Categoria_productos_Admin(admin.ModelAdmin) :
    list_display=('nombre','creado','actualizado')
    
    search_fields=('nombre','creado','actualizado')
    
    
class Productos_Admin(admin.ModelAdmin) :
    list_display=('nombre','precio','disponibilidad')
    search_fields=('nombre','precio','disponibilidad')
    
admin.site.register(Categoria_Producto,Categoria_productos_Admin)
admin.site.register(Productos,Productos_Admin)