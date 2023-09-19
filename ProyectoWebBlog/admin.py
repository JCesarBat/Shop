from django.contrib import admin

from ProyectoWebBlog.models import Post,Categoria
# Register your models here.t
class PostAdmin(admin.ModelAdmin):
    list_display=('titulo','creado','actualizado',)
    search_fields=('titulo','creado','actualizado',)


class CategoriaAdmin(admin.ModelAdmin):
    list_display=('categoria','creado','actualizado',)
    search_fields=('categoria','creado','actualizado',)

admin.site.register(Post,PostAdmin )

admin.site.register(Categoria,CategoriaAdmin )