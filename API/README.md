API Endpoints
-
La API de FaunaSV contiene los siguientes endpoints:

Login
-
La API tiene implementado un metodo de auténticacion por Token, para obtener dicho Token se realiza la siguiente 
petición como ejemplo:

    curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"username": "invitado", "password": "hcsKu64sBtNmzMJ"}' \
    https://faunaelsalvador.herokuapp.com/api/token/

Respuesta ejemplo:
    
    {
    "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU",
    "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
    }
Modificando el "username" y el "password" según sea el caso. En respuesta se obtendra un Token de acceso y uno de
refresco, cuando el Token expire debera enviar el de refresco para un nuevo Token. [Consultar documentacion para más información](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html).

/grupoanimal
-
API endpoint permite Mostrar los grupos de animales, crear o editarlos,
la opción de creación y edicion solo se encuentra disponible con auténticacion. Se puede interactuar con con el
siguiente enlace: https://faunaelsalvador.herokuapp.com/grupoanimal/

Método GET:
    
    Header: application/json
    Response:
        [
            {
                "nombre_grupo_animal": "Crocodylia"
            },
            {
                "nombre_grupo_animal": "Squamata"
            },
            {
                "nombre_grupo_animal": "Testudines"
            }
        ]

Método POST:

    Header: application/json
    Body:
    {
        "nombre_grupo_animal": "nombre"
    }
    
    Response: 200 OK
    Body:
        {
            "nombre_grupo_animal": "nombre"
        }
        
/familiaanimal
-
API endpoint permite mostrar las familias de animales o editarlas
la opción de edición solo se encuentra disponible con auténticacion. Se puede interactuar con con el
siguiente enlace: https://faunaelsalvador.herokuapp.com/familiaanimal/

Método GET:

    Header: application/json
    Response:
    [
        {
            "nombre_familia_animal": "Alligatoridae",
            "grupo_animal": {
                "nombre_grupo_animal": "Crocodylia"
            }
        },
        {
            "nombre_familia_animal": "Anguidae",
            "grupo_animal": {
                "nombre_grupo_animal": "Squamata"
            }
        },
        ...
    ]

Método POST:

    Header: application/json
    Body:
        {
            "nombre_familia_animal": "nombre_familia",
            "grupo_animal": {
                "nombre_grupo_animal": "nombre_grupo_animal"
            }
        }
    
    Response: 200 OK
        {
            "nombre_familia_animal": "nombre_familia",
            "grupo_animal": {
                "nombre_grupo_animal": "nombre_grupo_animal"
            }
        }
        
/especieanimal
-
API endpoint permite mostrar las especies animales o editarlas
la opción de edición solo se encuentra disponible con auténticacion. Se puede interactuar con con el
siguiente enlace: https://faunaelsalvador.herokuapp.com/especieanimal/

Método GET:

    Header: application/json
    Response:
        [
            {
                "nombre_especie_animal": "Abronia montecristoi",
                "familia_animal": {
                    "nombre_familia_animal": "Anguidae",
                    "grupo_animal": {
                        "nombre_grupo_animal": "Squamata"
                    }
                }
            },
            {
                "nombre_especie_animal": "Agkistrodon bilineatus",
                "familia_animal": {
                    "nombre_familia_animal": "Viperidae",
                    "grupo_animal": {
                        "nombre_grupo_animal": "Squamata"
                    }
                }
            },
            ...
        ]
    
Método POST:

    Header: application/json
    Body:
        {
            "nombre_especie_animal": "nombre especie animal",
            "familia_animal": {
                "nombre_familia_animal": "nombre familia animal",
                "grupo_animal": {
                    "nombre_grupo_animal": "nombre grupo animal"
                }
            }
        }
    
    Response: 200 OK
    {
        "nombre_especie_animal": "nombre especie animal",
        "familia_animal": {
            "nombre_familia_animal": "nombre familia animal",
            "grupo_animal": {
                "nombre_grupo_animal": "nombre grupo animal"
            }
        }
    }

/animal
-
API endpoint permite mostrar los distintos animales
la opción de edición solo se encuentra disponible con auténticacion
Se ha implementado el filtro search con los campos de nombre local y especie de animal
se puede acceder con /?search=. Se puede interactuar con con el
siguiente enlace: https://faunaelsalvador.herokuapp.com/animal/

Método GET:

    Header: application/json
    Response:
    [
    {
        "nombre_local": "Bebeleche de bosque",
        "estacionalidad": "Residente",
        "especie": {
            "nombre_especie_animal": "Anolis macrophallus",
            "familia_animal": {
                "nombre_familia_animal": "Dactyloidae",
                "grupo_animal": {
                    "nombre_grupo_animal": "Squamata"
                }
            }
        }
    },
    {
        "nombre_local": "Bebeleche de serrano",
        "estacionalidad": "Residente",
        "especie": {
            "nombre_especie_animal": "Anolis serranoi",
            "familia_animal": {
                "nombre_familia_animal": "Dactyloidae",
                "grupo_animal": {
                    "nombre_grupo_animal": "Squamata"
                }
            }
        }
    },
    ...
    ]

Método POST:

    Header: application/json
    Body:
    {
        "nombre_local": "nombre local",
        "estacionalidad": "estacionalidad",
        "especie": {
            "nombre_especie_animal": "nombre especie animal",
            "familia_animal": {
                "nombre_familia_animal": "nombre familia animal",
                "grupo_animal": {
                    "nombre_grupo_animal": "nombre grupo animal"
                }
            }
        }
    }
    
    Response: 200 OK
    {
        "nombre_local": "nombre local",
        "estacionalidad": "estacionalidad",
        "especie": {
            "nombre_especie_animal": "nombre especie animal",
            "familia_animal": {
                "nombre_familia_animal": "nombre familia animal",
                "grupo_animal": {
                    "nombre_grupo_animal": "nombre grupo animal"
                }
            }
        }
    }
    
/expertos
-
API endpoint permite mostrar, crear y modificar a los expertos,
se requiere de auténticacion para poder verlos. Se puede interactuar con con el
siguiente enlace: https://faunaelsalvador.herokuapp.com/expertos/

Método GET:

    Header: application/json
    Response:
    [
        {
            "id_experto": 1,
            "nombre_experto": "Nombre1",
            "apellido_experto": "Apellido1",
            "institucion_experto": "Institucion1",
            "identificacion_experto": "Identificacion2",
            "usuario": "FaunaSV_Admin"
        },
        ...
    ]

Método POST:

    Header: application/json
    Body:
    {
        "nombre_experto": "nombre experto",
        "apellido_experto": "apellido experto",
        "institucion_experto": "institucion experto",
        "identificacion_experto": "identificacion experto"
    }
    
    Response: 200 OK
    Body:
    {
        "id_experto": 1,
        "nombre_experto": "nombre experto",
        "apellido_experto": "apellido experto",
        "institucion_experto": "institucion experto",
        "identificacion_experto": "identificacion experto",
        "usuario": "invitado"
    }
    
/avistamientos
-
API endpoint permite mostrar, editar y crear los avistamientos
la opción de edición solo se encuentra disponible con auténticacion.
Se ha implementado el filtro search con los campos de username y nombre de animal
se puede acceder con /?search=. Se puede interactuar con con el
siguiente enlace: https://faunaelsalvador.herokuapp.com/avistamientos/

Método GET:

    Header: application/json
    Response:
    [
        {
            "id_avistamiento": 31,
            "geom": "SRID=4326;POINT (-89.19851303100583 13.68501846053549)",
            "confirmado": false,
            "fecha_hora": "2020-12-01T02:52:59Z",
            "fotografia": "https://faunaelsalvador.herokuapp.com/media/masacuata.jpeg",
            "descripcion": "Una masacuata",
            "usuario": "alexander",
            "animal": "Masacuata"
        },
        {
            "id_avistamiento": 32,
            "geom": "SRID=4326;POINT (-89.07646179199216 13.69135632238226)",
            "confirmado": false,
            "fecha_hora": "2020-12-01T02:54:15Z",
            "fotografia": "https://faunaelsalvador.herokuapp.com/media/caiman.jpeg",
            "descripcion": "Un caiman",
            "usuario": "CarlosSIG",
            "animal": "Caimán, caimán de anteojos"
        },
        ...
    ]
Método POST:

    Header: multipart/form-data or application/x-www-form-urlencoded    
    Body:
    {
        "geom": "SRID=4326;POINT (-89.24194335937494 13.68668633547035)",
        "confirmado": false,
        "fecha_hora": "2020-12-01T03:10:09Z",
        "fotografia": "imagen.jpg",
        "descripcion": "Descripcion",
        "animal": "Gecko leopardo"
    }
    
    Response: 200 OK
    Body:
    {
        "id_avistamiento": 31,
        "geom": "SRID=4326;POINT (-89.24194335937494 13.68668633547035)",
        "confirmado": false,
        "fecha_hora": "2020-12-01T03:10:09Z",
        "fotografia": "imagen.jpg",
        "descripcion": "Descripcion",
        "usuario": "invitado",
        "animal": "Gecko leopardo"
    }

/getcercanos
-
API View que permite obtener los id de los avistamientos mas ceranos,
recibiendo un string point que hace referencia a una geometría vector punto, y
delimitado por la variable string km, que hace referencia a la cantidad
de metros que se extenderá la busqueda. El resultado obtenido es una lista de enteros.
Ejemplo:
        
        https://faunaelsalvador.herokuapp.com/getcercanos/point=SRID=4326;POINT (-89.24194335937494 13.68668633547035)&m=23
        
        Response: 200 OK 
        [
            1,
            2,
            3
        ]
        
/getdistpuntos
-
API View que permite calcular la distancia entre dos geometrias
WGS84 - SRID 4326, recibe una string point1 que es un objeto espacial vector punto,
tambien recibe una string point2 que es un objeto espacial de tipo vector punto.
El resultado obtenido es un flotante representando la distancia en metros.
Ejemplo:

    https://faunaelsalvador.herokuapp.com/getdistpuntos/point1=SRID=4326;POINT (-89.24194335937494 13.68668633547035)&point2=SRID=4326;POINT (-89.07646179199216 13.69135632238226)
    
    Response 200 OK:
    [5000]