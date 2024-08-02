from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductoSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategoriaSerializer

class ordenesViewSet(viewsets.ModelViewSet):
    queryset = Ordenes.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrdenesSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CalificacionSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClienteSerializer
