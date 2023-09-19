from django.db import models


# Create your models here.


class Servicos(models.Model):
    titulo=models.CharField(max_length=255)
    contenido=models.CharField(max_length=255)
    imagen=models.ImageField(upload_to='servicios')
    creado=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo 