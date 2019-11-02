import subprocess
import shlex
from django.conf import settings
from DatabaseBackup.celery import app
from celery import task 

@task(name='run_script') 
def run_script(id):
    system=Sistema.objects.get(id_system=pk)
    respados=CopiaRespaldo.objects.filter(id_system=system)

    for i in respados:
        subprocess.call(shlex.split('./Scripts/move_backup.sh system.server_username system.server_ip system.server_password system.server_route_save i.receptor_password system.server_route_save system.bd_name i.receptor_server_username i.receptor_server_ip i.receptor_route_save'))
        