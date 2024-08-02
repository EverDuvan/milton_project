from rest_framework import routers
from .api import *
from django.urls import path
from django.urls import include

routers = routers.DefaultRouter()
routers.register('api/productos', ProductosViewSet, 'productos')
routers.register('api/categorias', CategoriasViewSet, 'categorias')
routers.register('api/ordenes', ordenesViewSet, 'ordenes')
routers.register('api/calificacion', CalificacionViewSet, 'calificacion')
routers.register('api/cliente', ClientesViewSet, 'carrito')

urlpatterns = [
    path('', include(routers.urls))
]

urlpatterns += routers.urls