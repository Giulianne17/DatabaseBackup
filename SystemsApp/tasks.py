import subprocess
import shlex
from django.conf import settings
from DatabaseBackupApp.celery import app
from celery import task 
from SystemsApp.models import *
from DatabaseBackupApp.settings import BASE_DIR
import os

@app.task(name="run_script")
def run_script(pk):
    system=Sistema.objects.get(id_system=int(pk))
    respados=CopiaRespaldo.objects.filter(id_system=system)
    p=BASE_DIR.split("/")
    path=""
    for j in p[:len(p)-1]:
        path= path + str(j)+"/"
    for i in respados:
        subprocess.call(shlex.split('./Scripts/move_backup.sh '+ str(system.server_username)+ ' '+ str(system.server_ip)+ ' '+ str(system.server_password)+ ' '+ str(system.server_route_save)+ ' '+ str(i.receptor_password)+ ' '+ str(system.bd_name)+ ' '+ str(i.receptor_server_username)+ ' '+ str(i.receptor_server_ip)+ ' '+ str(i.receptor_route_save)+' '+str(path)))
    return True  
