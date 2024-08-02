from django.db import models

class Productos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categorias_id = models.ForeignKey('Categorias', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class Ordenes(models.Model):
    OPCIONES_ESTADO = [
        ('P', 'Pendiente'),
        ('A', 'Aprobada'),
        ('R', 'Rechazada'),
        ]
    id = models.AutoField(primary_key=True)
    fecha = models.DateField()
    clientes_id = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    estado = OPCIONES_ESTADO
    Productos_id = models.ForeignKey('Productos', on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha
    
class Calificacion(models.Model):
    id = models.AutoField(primary_key=True)
    Clientes_id = models.ForeignKey('Clientes', on_delete=models.CASCADE)
    Productos_id = models.ForeignKey('Productos', on_delete=models.CASCADE)
    calificacion = models.IntegerField()
    contenido = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.fecha

class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    correo = models.EmailField()
    telefono = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre