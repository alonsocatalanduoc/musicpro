from django.urls import path
# En sucursal/urls.py
from .views import data, producto_index, pagar, list_boleta, index  # Corrige el nombre de la función aquí

urlpatterns = [
    path('producto_index/', producto_index, name="sucursal_producto_index"),

    path('data', data, name="sucursal_data"),
    path('pagar', pagar, name="pagar"),
    path('list_boleta', list_boleta, name="list_boleta"),
    path('', index, name="sucursal_index"),
]
