# DatabaseBackup

## Aplicación para mover un backup de una bd de un servidor a otro o drive

SystemsApp es una mini aplicación web para el manejo de los sistemas donde se guardan los backups a mover.

La aplicación actualmente se encuentra en el siguiente [link de acceso](https://movedatabasebackup.herokuapp.com).

Está desarrollada en Django 2.2.3 y tiene las siguientes funcionalidades:

* Registrar sistemas
* Editar los sistemas 
* Eliminar los sistemas
* Obtener la lista de los sitemas 
* Ver detalles de un sistema.
* Registrar servidores/drive donde se haran la copia
* Editar servidores/drive donde se haran la copia
* Eliminar servidores/drive donde se haran la copia
* Obtener la lista de los servidores/drives donde se enviara el backup 
* Ver detalles de los servidores/drives donde se enviara el backup 

## Instalación

Primero asegúrese de instalar:

* PostgreSQL (9.5.14)
* Virtualenv (16.0.0)
* Python (3.6.9)
* pip (19.3.1)
* sshpass
* Redis

### Configuración de un entorno virtual

Cree un nuevo entorno virtual en la carpeta del proyecto con python3 por defecto:

```
virtualenv env --python=$(which python3)
```

Para activar el entorno:
```
source env/bin/activate
```

Para desactivar el entorno:
```
deactivate
```

Para instalar los paquetes necesarios:
```
pip install -r requirements.txt
```

### Configuración de la base de datos / migraciones

Para configurar la base de datos se tiene el script `installdb.sh` y para aplicar las migraciones `migrate.sh`.

Para otorgar los permisos necesarios de ejecución:
```
chmod +x installdb.sh migrate.sh
```

Ahora para configurar la base de datos, ejecute:
```
./installdb.sh
```

Y para aplicar las migraciones y actualizar la base de datos:
```
./migrate.sh
```

### Para ejecutar la aplicación

En una terminal se debe ejecutar el servidor de python con el comando:

```
python manage.py runserver
```

En paralelo en otra terminal se debe ejecutar el celery para que se realicen las tareas:

```
celery -A DatabaseBackupApp worker --beat --scheduler django --loglevel=info
```

### Ejemplo json

En la tabla de Sistemas:

{
        "id_system": 1,
        "name": "Sistema 1",
        "bd_name": "backup.sql",
        "bd_type": "postgresql",
        "frequency": 11,
        "type_frequency": "minutes",
        "server_ip": "192.168.1.107",
        "server_username": "user",
        "server_password": "password",
        "server_route_save": "home/",
        "copy_to_server": true,
        "copy_to_drive": true
}

Observación: Si tiene las opciones de copy_to_server o copy_to_drive en false, no se movera el respaldo a dicha opción. 

En la tabla de CopiaRespaldo:

{
        "id_respaldo": 1,
        "id_system": 1,
        "receptor_server_username": "user2",
        "receptor_password": "password2",
        "receptor_server_ip": "192.168.1.107",
        "receptor_route_save": "home/w/"
}

Observación: en esta última tabla se puede almacenar los drive y los servidores.
