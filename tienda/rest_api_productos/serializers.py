from rest_framework import serializers
from sucursal.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Producto
        fields = [ 'nombre', 'descripcion', 'precio' ]

        