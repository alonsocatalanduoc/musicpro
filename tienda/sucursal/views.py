from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Producto, Boleta, DetalleBoleta
from faker import Faker
import json

fake = Faker()

def producto_index(request):
    productos = Producto.objects.all()
    return render(request, 'sucursal/producto_index.html', {"productos": productos})

def data(request):
    for _ in range(100):
        Producto.objects.create(
            nombre=fake.word(),
            descripcion=fake.text(),
            precio=fake.random_int(min=1, max=100),
        )

    return JsonResponse({'mensaje': 'Datos generados con éxito'})



def pagar(request):
    if request.method == 'POST':
        # Obtener los datos del formulario POST
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        productos_form = request.POST.get('productos_form')
        productos_form = json.loads(productos_form)

        total = 0
        

        # Calcular el precio total
        for item in productos_form:
            producto_id = item.get('id')
            producto = Producto.objects.get(pk=producto_id)
            cantidad = item.get('cantidad', 1)
            total += producto.precio * cantidad

        # Verificar que el precio total sea mayor que 0
        if total > 0:
            boleta = Boleta.objects.create(
                precio_total=total,
                nombre_usuario=nombre,
                direccion_usuario=direccion
            )

            compras = []  # Lista para almacenar detalles de compra

            for item in productos_form:
                producto_id = item.get('id')
                producto = Producto.objects.get(pk=producto_id)
                cantidad = item.get('cantidad', 1)

                # No guardar la compra si la cantidad es 0
                if cantidad > 0:
                    detalle = DetalleBoleta.objects.create(
                        boleta=boleta,
                        producto=producto,
                        cantidad=cantidad,
                        precio_unitario=producto.precio,
                        precio_total=producto.precio * cantidad
                    )
                    compras.append(detalle)

            # Verificar que haya compras antes de guardar la boleta
            if compras:
                boleta.precio_total = sum(detalle.precio_total for detalle in compras)
                boleta.save()

                return render(request, 'sucursal/boleta.html', {
                    'nombre_usuario': boleta.nombre_usuario,
                    'direccion_usuario': boleta.direccion_usuario,
                    'compras': compras,
                    'precio_total': boleta.precio_total
                })
                

        # Si el precio total es 0, no realizar la compra
        return HttpResponse("Error: El precio total es 0. No se realizó la compra.")
    

    # Manejar la lógica para GET si es necesario
    return HttpResponse("Esta vista solo responde a peticiones POST.")


def list_boleta(request):
    boletas = Boleta.objects.all()
    return render(request, 'sucursal/list_boleta.html', {"boletas": boletas})

def index(request):
    return render(request, 'sucursal/index.html')
