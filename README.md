# Olimpres
> más cerca de ti...

Plataforma digital para acercar los servicios de Olistudio a ti. 
Desarrollada con mucho empeño y con el ánimo de que nuestros servicios sean de excelencia :D 

## Installing / Getting started

Esta App está desarrollada en Django y soportada en Docker. Solo se necesita tener Docker instalado y clonar el repositorio. 

```shell
git clone https://github.com/rejamen/olimpres.git
cd olimpres
docker-compose up
```

Ahora puedes acceder al navegador https://localhost:8000 y verás nuestra página principal.

### Algunos tips útiles sobre Olimpres Docker-Django app
* Detener la App después de hacer docker-compose up
```shell
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.  
```
* Comprobar la versión de Django que se está usando
```shell
docker-compose run web python3 -m django --version  
```
* Conectarse al contenedor de Django
```shell
docker-compose exec -u root web bash 
# entra por defecto a la ruta /code donde está el 
# código fuente de la App 
```
* Conectarse al contenedor de Postgres y a la BD usada
```shell
docker-compose exec -u root db bash   # entra al container
psql -U postgres -d olimpres          # se conecta a la BD
```
* Entrar/Salir en modo Django Shell
```shell
docker-compose run web python3 manage.py shell  # inicia shell mode
CTRL + C                                         # para salir
```
* Crear una App nueva en el proyecto
```shell
docker-compose run web python3 manage.py startapp <NombreApp>   
```
* Migrate / Makemigration
```shell
docker-compose run web python3 manage.py migrate
docker-compose run web python3 manage.py makemigrations   
```
* Create superuser
```shell
docker-compose run web python3 manage.py createsuperuser
```


