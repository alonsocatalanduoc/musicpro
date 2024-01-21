from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Boleta(models.Model):
    fecha_emision = models.DateField(auto_now_add=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_usuario = models.CharField(max_length=255)
    direccion_usuario = models.CharField(max_length=255)
    codigo_seguimiento = models.CharField(blank=True,null=True,max_length=255)
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Añade el campo de usuario

class DetalleBoleta(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.precio_total = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def total(self):
        return self.cantidad * self.precio_total

