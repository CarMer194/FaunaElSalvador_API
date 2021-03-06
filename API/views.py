from django.db import connection
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, filters, status
from rest_framework import permissions
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import *
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django.core.files.storage import default_storage
import logging


# Create your views here.


@api_view(['GET'])
def obtener_avistamientos_cercanos(request, point, km):
    """API View que permite obtener los id de los avistamientos mas ceranos,
    recibiendo un string point que hace referencia a una geometria vector punto, y
    delimitado por la variable string km, que hace referencia a la cantidad
    de metros que se extenderá la busqueda. El resultado obtenido es una lista de enteros"""
    grados = int(km)/111000
    grados = str(grados)
    print(grados)
    lista = []
    try:
        avistamientos = Avistamiento.objects.raw(
            'SELECT id_avistamiento FROM "API_avistamiento" as av WHERE st_contains(st_buffer(%s,%s),av.geom)',
            [point, grados])
        for avi in avistamientos:
            lista.append(avi.id_avistamiento)
    except Avistamiento.DoesNotExist:
        return Response(status=404)
    print(lista)
    return Response(lista, status=200)


@api_view(['GET'])
def obtener_distancia_objeto(request, point1, point2):
    """API View que permite calcular la distancia entre dos geometrias
    WGS84 - SRID 4326, recibe una string point1 que es un objeto espacial vector punto,
    tambien recibe una string point2 que es un objeto espacial de tipo vector punto.
    El resultado obtenido es un flotante representando la distancia en metros"""
    distancia2 = None
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT ST_Distance(ST_Transform(%s::geometry, 4326),ST_Transform(%s::geometry, 4326));', [point1, point2])
        distancia = cursor.fetchone()
        distancia2 = float(distancia[0]) * 111000
    return Response(distancia2, status=200)


class GrupoAnimalView(viewsets.ModelViewSet):
    """
    API endpoint permite Mostrar los grupos de animales, crear o editarlos,
    la opción de creación y edicion solo se encuentra disponible con auténticacion.
    """
    queryset = Grupo_Animal.objects.all().order_by('nombre_grupo_animal')
    serializer_class = GrupoAnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FamiliaAnimalView(viewsets.ModelViewSet):
    """
    API endpoint permite mostrar las familias de animales o editarlas
    la opción de edición solo se encuentra disponible con auténticacion
    """
    queryset = Familia_Animal.objects.all().order_by('nombre_familia_animal')
    serializer_class = FamiliaAnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EspecieAnimalView(viewsets.ModelViewSet):
    """
    API endpoint permite mostrar las especies animales o editarlas
    la opción de edición solo se encuentra disponible con auténticacion
    """
    queryset = Especie_Animal.objects.all().order_by('nombre_especie_animal')
    serializer_class = EspecieAnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AnimalView(viewsets.ModelViewSet):
    """
    API endpoint permite mostrar los distintos animales
    la opción de edición solo se encuentra disponible con auténticacion
    Se ha implementado el filtro search con los campos de nombre local y especie de animal
    se puede acceder con /?search=
    """
    queryset = Animal.objects.all().order_by('nombre_local')
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre_local', 'especie__nombre_especie_animal']


class ExpertoView(viewsets.ModelViewSet):
    """
    API endpoint permite mostrar a los expertos
    se requiere de auténticacion para poder verlos
    """
    queryset = Experto.objects.all().order_by('id_experto')
    serializer_class = ExpertoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class AvistamientoView(viewsets.ModelViewSet):
    """
    API endpoint permite mostrar, editar y crear los avistamientos
    la opción de edición solo se encuentra disponible con auténticacion.
    Se ha implementado el filtro search con los campos de username y nombre de animal
    se puede acceder con /?search==
    """
    queryset = Avistamiento.objects.all().order_by('id_avistamiento')
    serializer_class = AvistamientoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['usuario__username', 'animal__nombre_local']
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        logger = logging.getLogger(__name__)
        logger.info(self.request.data)
        logger.info(self.request.FILES)
        print(self.request.data)
        print(self.request.FILES)
        serializer.save(usuario=self.request.user)

    def post(self, request, *args, **kwargs):

        print("hola")
        print(request.FILES)
        avistamiento_serializer = AvistamientoSerializer(data=request.data)
        if avistamiento_serializer.is_valid(raise_exception=True):
            print(avistamiento_serializer.data())
            Avistamiento.save(avistamiento_serializer.data, request.FILES)
            file = request.FILES
            file_name= default_storage.save(file.name, file)
            return Response(avistamiento_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(avistamiento_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
