from .models import Mantenimiento_Tipo, Mantenimiento_Vehiculo
from rest_framework import serializers

class Mantenimiento_Tipo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento_Tipo
        fields = ('id', 'nombre')

class Mantenimiento_Vehiculo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento_Vehiculo
        fields = ('id', 'observacion','fecha','fecha_futura','km','tipo_mantenimiento_id','vehiculo_id')