from django.db import models

from django.contrib.auth.models import User

# Create your models here.



class Categoria(models.Model):
    categoria=models.CharField(max_length=255)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return self.categoria
    
    
    
class Post(models.Model):
    titulo=models.CharField(max_length=255)
    contenido=models.CharField(max_length=255)
    imagen=models.ImageField(upload_to='blog',blank=True,null=True)
    autor=models.ForeignKey(User,on_delete=models.CASCADE)
    
    relacion=models.ManyToManyField(Categoria)
    
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return self.titulo