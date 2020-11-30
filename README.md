FaunaSV API
-
FaunaSV es un proyecto basado en GeoDjango y PostGIS para el registro
de la fauna de El Salvador con enfoque geoespacial.

Requisitos
-
    -Python(3.5, 3.6, 3.7, 3.8, 3.9)
    -Django (3.0,3.1)
    -djangorestframework
    -dj-database-url
    -psycopg2
    -python-decouple
    -whitenoise
    -drf-writable-nested
    -Pillow
    -djangorestframework-simplejwt
    -django-filter
    Para su despliegue en heroku se han utilizado:
    -django-heroku
    -gunicorn

Pasos para su instalacion
-
    pip3 install requirements.txt

Dirigirse a FaunaEsSalvador_API/setting.py, en la parte de DATABASES configurar la base de datos para su conexión,
es requisito un base de datos PostgreSQL con extensión PostGIS.

Luego crear las migraciones:

    python3 manage.py makemigrations
    python3 manage.py migrate
Cree un superusuario para el panel de administración:
    
    python3 manage.py createsuperuser
Configurar la cuenta de usuario y luego correr el servidor:

    python3 manage.py runserver
    
API
-
FaunaSV API se ha construido basandonos en el framework [Django](https://www.djangoproject.com/) 
y [DjangoRestFramework](https://www.django-rest-framework.org/)

-   Autenticacion de usuarios a traves de JSON, se realiza con la implementación de la libreria [SimpleJWT](https://github.com/SimpleJWT/django-rest-framework-simplejwt),
    ejemplo:
    
        curl \
        -X POST \
        -H "Content-Type: application/json" \
        -d '{"username": "torogoz", "password": "volador"}' \
        http://localhost:8000/api/token/
    Se recibirá dos tokens para autenticación y para actualización:
    
        {
        "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU",
        "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
        }
    Para mas información consulte la documentación: [SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html)
    