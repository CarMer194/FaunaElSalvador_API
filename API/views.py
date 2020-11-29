from django.db import connection
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET'])
def obtener_avistamientos_cercanos(request, point, km):
    grados = km/111000
    lista = []
    try:
        avistamientos = Avistamiento.objects.raw('SELECT id_avistamiento FROM "API_avistamiento" as av WHERE st_contains(st_buffer(%s,%s),av.geom)', [point, grados])
        for avi in avistamientos:
            lista.append(avi.id_avistamiento)
    except Avistamiento.DoesNotExist:
        return Response(status=404)
    print(lista)
    return Response(lista, status=200)


class GrupoAnimalView(viewsets.ModelViewSet):
    """
    API endpoint permite Mostrar los grupos de animales o editarlos
    """
    queryset = Grupo_Animal.objects.all().order_by('nombre_grupo_animal')
    serializer_class = GrupoAnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FamiliaAnimalView(viewsets.ModelViewSet):
    """
    API endpoint permite mostrar las familias de animales o editarlas
    """
    queryset = Familia_Animal.objects.all().order_by('nombre_familia_animal')
    serializer_class = FamiliaAnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EspecieAnimalView(viewsets.ModelViewSet):
    """
    API endpoint permite mostrar las especies animales o editarlas
    """
    queryset = Especie_Animal.objects.all().order_by('nombre_especie_animal')
    serializer_class = EspecieAnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AnimalView(viewsets.ModelViewSet):
    """
    API endpoint permite mostrar los distintos animales
    """
    queryset = Animal.objects.all().order_by('nombre_local')
    serializer_class = AnimalSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre_local', 'especie__nombre_especie_animal']


class ExpertoView(viewsets.ModelViewSet):
    """
    API endpoint permite mostrar a los expertos
    """
    queryset = Experto.objects.all().order_by('id_experto')
    serializer_class = ExpertoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class AvistamientoView(viewsets.ModelViewSet):
    """
    API endpoint permite mostrar los avistamientos
    """
    queryset = Avistamiento.objects.all().order_by('id_avistamiento')
    serializer_class = AvistamientoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['usuario__username', 'animal__nombre_local']



    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
