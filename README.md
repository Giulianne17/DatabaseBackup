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





