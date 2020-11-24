from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from drf_writable_nested.serializers import WritableNestedModelSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GrupoAnimalSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Grupo_Animal
        fields = [
            'idGrupo',
            'nombre_grupo_animal',
        ]
        read_only_fields = ('idGrupo',)


class FamiliaAnimalSerializer(WritableNestedModelSerializer):
    grupo_animal = GrupoAnimalSerializer(allow_null=False)

    class Meta:
        model = Familia_Animal
        fields = [
            'id_familia_animal',
            'nombre_familia_animal',
            'grupo_animal',
        ]
        read_only_fields = ('id_familia_animal',)


class EspecieAnimalSerializer(WritableNestedModelSerializer):
    familia_animal = FamiliaAnimalSerializer(allow_null=False)

    class Meta:
        model = Especie_Animal
        fields = [
            'id_especie_animal',
            'nombre_especie_animal',
            'familia_animal',
        ]
        read_only_fields = ('id_especie_animal',)


class AnimalSerializer(WritableNestedModelSerializer):
    especie = EspecieAnimalSerializer(allow_null=False)

    class Meta:
        model = Animal
        fields = [
            'id_Animal',
            'nombre_local',
            'estacionalidad',
            'especie',
        ]
        read_only_fields = ('id_Animal',)


class ExpertoSerializer(WritableNestedModelSerializer):
    usuario = UserSerializer(allow_null=False)

    class Meta:
        model = Experto
        fields = [
            'id_experto',
            'nombre_experto',
            'apellido_experto',
            'institucion_experto',
            'identificacion_experto',
            'usuario',
        ]
        read_only_fields = ('id_experto', 'usuario',)


class AvistamientoSerializer(WritableNestedModelSerializer):
    usuario = UserSerializer()
    animal = AnimalSerializer

    class Meta:
        model = Avistamiento
        fields = [
            'id_avistamiento',
            'geom',
            'confirmado',
            'fecha_hora',
            'fotografia',
            'descripcion',
            'usuario',
            'animal',
        ]
        read_only_fields = ('id_avistamiento',)
