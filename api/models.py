from django.db import models

class Mantenimiento_Tipo(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__ (self): 
        return self.nombre
    descripcion = models.CharField(max_length=500)
    def __str__ (self): 
        return self.descripcion

class Mantenimiento_Vehiculo(models.Model):
    observacion = models.CharField(max_length=200)
    fecha = models.DateField('Fecha')
    fecha_futura = models.DateField('Proxima Revision')
    km = models.IntegerField(default=0)
    tipo_mantenimiento_id = models.ForeignKey(Mantenimiento_Tipo,on_delete=models.CASCADE)
    vehiculo_id = models.IntegerField(default=0)

    def __str__ (self): 
        return self.observacion
