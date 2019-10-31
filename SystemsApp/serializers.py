from rest_framework import serializers
from .models import *

class SistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sistema
        fields = ('id_system','name','bd_name','bd_password','bd_username','bd_type','frequency','type_frequency','server_ip','server_username','server_password','server_route_save')


class CopiaRespaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CopiaRespaldo
        fields = ('id_respaldo','id_system','receptor_server_username','receptor_server_ip','receptor_route_save')

