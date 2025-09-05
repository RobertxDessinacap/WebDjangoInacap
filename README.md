# WebDjangoInacap
Actividad en parejas Back-End Roberto Yañez, Juan Sanhueza
Profesor: Emilio Gonzalo Soto Rojas
Asignatura:2025/P Programación Back End (TI3V41/V-ICS-N4-P2-C1(F)/V Santiago Sur IEC)
## Usando DJANGO 

La pagina consta con 3 paginas, La pagina en común, y 2 paginas personales que reutilizamos en la asignatura de Front-End.
En django se creo el proyecto usando 
```bash
django-admin startproject WebDjango Django
```
De esta forma se creó el proyecto donde trabajamos.

Luego utilizamos el comando
```bash
py manage.py startapp JR 
```
Creando así la aplicación.

En JR creamos 2 carpetas,
"templates" para colocar ahí los archivos HTML y "static" donde se encontraran los archivos CSS y JS, ademas de algunas imagenes que se utilizaran dentro de las paginas.

En este punto, en la terminal ejecutamos el siguiente codigo
```bash
py manage.py migrate
```
para generar la base de dato por defecto en SQLITE.
Luego ejecutar
```bash
py manage.py createsuperuser
```
> #### Credenciales de /admin
> -Juan:asd123
> -Roberto:asd123

Y para poder ver las paginas ejecutamos en la terminal
```bash
py manage.py runserver
```

De esta manera completamos el levantamiento del servidor local con Django.

En este punto comenzamos a trabajar con los archivos de Python (.py)
Dentro de la carpeta creada al inicio "WebDjango" en el archivo "settings.py" en la lista de "INSTALLED_APPS" agregamos el nombre de la carpeta de la app para que Django la pueda reconocer correctamente.

#POR CONTINUAR
