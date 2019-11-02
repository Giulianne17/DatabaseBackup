from rest_framework import serializers
from .models import *

class SistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sistema
        fields = ('id_system','name','bd_name','bd_type','frequency','type_frequency','server_ip','server_username','server_password','server_route_save','copy_to_server','copy_to_drive')


class CopiaRespaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopiaRespaldo
        fields = ('id_respaldo','id_system','receptor_server_username','receptor_password','receptor_server_ip','receptor_route_save')

