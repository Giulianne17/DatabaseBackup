import subprocess
import shlex
from django.conf import settings
from DatabaseBackupApp.celery import app
from celery import task 
from SystemsApp.models import *
from DatabaseBackupApp.settings import BASE_DIR
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

@app.task(name="run_script")
def run_script(pk):
    system=Sistema.objects.get(id_system=int(pk))
    respados=CopiaRespaldo.objects.filter(id_system=system)
    p=BASE_DIR.split("/")
    path=""
    for j in p[:len(p)-1]:
        path= path + str(j)+"/"
    for i in respados:
        if (not system.copy_to_server) and i.receptor_type=="server":
            pass
        elif (not system.copy_to_drive) and i.receptor_type=="drive":
            pass  
        else:
            subprocess.call(shlex.split('./Scripts/move_backup.sh '+ str(system.server_username)+ ' '+ str(system.server_ip)+ ' '+ str(system.server_password)+ ' '+ str(system.server_route_save)+ ' '+ str(i.receptor_password)+ ' '+ str(system.bd_name)+ ' '+ str(i.receptor_server_username)+ ' '+ str(i.receptor_server_ip)+ ' '+ str(i.receptor_route_save)+' '+str(path)))
    
    # Si hace la copia en drive.
    if system.copy_to_drive:
        #Se trae el archivo.
        subprocess.call(shlex.split('./Scripts/drive_backup.sh '+ str(system.server_username)+ ' '+ str(system.server_ip)+ ' '+ str(system.server_password)+ ' '+ str(system.server_route_save)+ ' '+ str(system.bd_name)+ ' '+str(path)))
                
        #Accede al drive
        g_login = GoogleAuth()
        g_login.LocalWebserverAuth()
        drive = GoogleDrive(g_login)
        
        #Mueve el archivo
        file1 = drive.CreateFile({'title': str(system.bd_name)})  # Create GoogleDriveFile instance with title 'Hello.txt'.
        file1.SetContentFile(str(path)+ str(system.bd_name)) # Set content of the file from given string.
        file1.Upload()

    return True  
