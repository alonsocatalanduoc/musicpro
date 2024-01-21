from django.urls import path
from . import views

#api/
urlpatterns = [
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/<id>', views.vista_productos, name='vista_productos'),
    
]
