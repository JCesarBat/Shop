from django.shortcuts import render

# Create your views here.

from ProyectoWebBlog.models import Post
from ProyectoWebBlog.models import Categoria
  
def blog_name(request):
    
    
    
    todos_blog=Post.objects.all()

    diccionario={"llave":"Esta es el Blog",'blog':todos_blog}
    
    return render(request,'ProyectoWebBlog/Plantillas/blog.html',diccionario)



def categoria_name (request,categoria_id):
    
    cate=Categoria.objects.get(id=categoria_id)
    
    
    post=Post.objects.filter(relacion=cate)
    diccionario={"llave":"Categoria",'post':post}
    
    return render(request,'ProyectoWebBlog/Plantillas/categorias.html',diccionario)
    
    
    