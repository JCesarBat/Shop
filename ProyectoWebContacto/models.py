from django.db import models

# Create your models here.

class GuardarInfo(models.Model):
    nombre=models.CharField(max_length=50)
    email=models.EmailField()
    contenido=models.CharField(max_length=1000)
    
    

