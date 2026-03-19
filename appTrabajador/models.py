from django.db import models

# Create your models here.
class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nombre_cargo
    
class Trabajador(models.Model):
   nombre_trabajador=models.CharField(max_length=100)
   ci=models.CharField(max_length=20, unique=True)
   telefono=models.CharField(max_length=20, blank=True, null=True)
   Cargo=models.ForeignKey(Cargo, on_delete=models.CASCADE)
   fecha_contratacion=models.DateField()
   def __str__(self):
       return self.nombre_trabajador