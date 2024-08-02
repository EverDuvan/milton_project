from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Productos)
admin.site.register(Categorias)
admin.site.register(Ordenes)
admin.site.register(Calificacion)
admin.site.register(Clientes)