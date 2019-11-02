from django.contrib import admin
from SystemsApp.models import *
# Register your models here.


class SistemaAdmin(admin.ModelAdmin):
	list_display =['id_system','name','bd_name','bd_type','frequency','type_frequency','server_ip','server_username','server_password','server_route_save','copy_to_server','copy_to_drive']

class CopiaRespaldoAdmin(admin.ModelAdmin):
	list_display =['id_respaldo','id_system','receptor_server_username','receptor_password', 'receptor_server_ip','receptor_route_save']

# Sistemas
admin.site.register(Sistema, SistemaAdmin)
# Servidores donde se guardaran las copias.
admin.site.register(CopiaRespaldo, CopiaRespaldoAdmin)

