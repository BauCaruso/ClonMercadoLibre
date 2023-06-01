from django.db import models

class Usuario(models.Model):
    nombre_de_usuario = models.CharField(max_length=200) 
    mail = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.nombre_de_usuario


class Item(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=1000)
    imagen = models.CharField(max_length=10000)  
    stock = models.IntegerField()
    vendedor = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    cantidad_de_ventas = models.IntegerField(default=0)
    veces_vendido = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.titulo
    
class Carrito(models.Model):
    nombre_carrito = models.CharField(max_length=)
    usuario_del_carrito: models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    items_del_carrito: models.ManyToManyField(Item)
# Create your models here.
