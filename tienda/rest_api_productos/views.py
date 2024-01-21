from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.parsers import JSONParser

from sucursal.models import Producto
from .serializers import ProductoSerializer


# Create your views here.

@csrf_exempt
@api_view(('GET', 'POST'))
def lista_productos(request):
    # mostrar todos los productos
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(('GET', 'PUT', 'DELETE'))
def vista_productos(request, id):
    # mostrar producto en particular
    if request.method == 'GET':
        try:
            producto = Producto.objects.get(id=id)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        try:
            producto = Producto.objects.get(id=id)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        try:
            producto = Producto.objects.get(id=id)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#@csrf_exempt
#@api_view(('POST'))
#def lista_productos(request):
#    print(request.data)
    
#    nombre = request.data[ 'Nombre' ]
#    descripcion = request.data[ 'Descripcion' ]
#    precio = request.data[ 'Precio' ]
    
#    print(f"estos son todos los productos {nombre}")
    
#    return Response(request.data)

