FaunaSV API
-
FaunaSV es un proyecto basado en GeoDjango y PostGIS para el registro
de la fauna de El Salvador con enfoque geoespacial. El proyecto contiene una base de datos de animales que residen
en El Salvador, se adjunta un archivo en PDF el recurso suministrado por el Ministerio de Medioambiente y Recursos 
Naturales, ademas de un backup en CSV contiendo los animales que se encuentran en la base de datos actualmente.

Requisitos
-
    -Python(3.5, 3.6, 3.7, 3.8, 3.9)
    -Django (3.0,3.1)
    -djangorestframework
    -psycopg2
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

Consideraciones
-
*   Actualmente el proyecto solo cuenta en su base de datos reptiles, se invita a continuar el registro de animales proveido
por el ministerio, realizando la extracción de datos del PDF.
*   El registro de usuarios no se encuentra habilitado, revisar la documentación de [Django](https://www.djangoproject.com/)
para obtener información sobre como habilitarla.

API
-
Sobre información de los API Endpoint consultar el documento que se encuentra en el repositorio.

Reconocimiento a liberias implementadas
-
*   DRF Writable Nested:
    Copyright (c) 2014-2020, beda.software All rights reserved.
    
*   Django Rest Framework:
    Copyright © 2011-present, Encode OSS Ltd. All rights reserved.
    
*   Django: Copyright (c) Django Software Foundation and individual contributors.
All rights reserved.

*   whitenoise: The MIT License (MIT) Copyright (c) 2013 David Evans

*   django-filter: Copyright (c) Alex Gaynor and individual contributors.
All rights reserved.

*   gunicorn: 2009-2018 (c) Benoît Chesneau <benoitc@e-engura.org>
2009-2015 (c) Paul J. Davis <paul.joseph.davis@gmail.com>