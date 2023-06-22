from django.contrib import admin

from .models import Mantenimiento_Tipo
from .models import Mantenimiento_Vehiculo

# Register your models here.

admin.site.register(Mantenimiento_Tipo)
admin.site.register(Mantenimiento_Vehiculo)