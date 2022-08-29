# Applicación web de sistema de riesgos
## Desarrolado con django 

## Instalacion de la aplicacion

Instalar python
Instalar librerias para ello colocarse en la raiz del proyecto y ejecutar:
```sh
pip install -r requirements.txt
```
Crear un superusuario para acceder al panel de administracion
```sh
python manage.py createsuperuser
```
Migrar base de datos
```sh
python manage.py makemigrations
python manage.py migrate
```
Levantar el servidor
```sh
python manage.py runserver
```


### En caso de error activar el modo de prueba...
Ingresar a settings.py dentro de la carpeta app y cambiar:
```sh
DEBUG=False
```