from django.contrib import admin

from ProyectoWebbServicios.models import Servicos



# Register your models here.


class ServiciosAdmin(admin.ModelAdmin):
    list_display=('titulo','creado','updated',)
    search_fields=('titulo','creado','updated',)


admin.site.register(Servicos,ServiciosAdmin)