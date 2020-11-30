from django.contrib.auth.models import User
from drf_writable_nested import UniqueFieldsMixin, NestedUpdateMixin, NestedCreateMixin
from rest_framework import serializers, generics
from .models import *
from drf_writable_nested.serializers import WritableNestedModelSerializer
"""Clase donde estan implementados los serializadores de los modelos"""


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador del modelo user con los campos: id, username, email, groups, experto, avistamiento, password
    donde el campo id es solo lectura y el campo password solo escritura.
    """
    experto = serializers.PrimaryKeyRelatedField(many=True , queryset=Experto.objects.all())
    avistamiento = serializers.PrimaryKeyRelatedField(many=True, queryset=Avistamiento.objects.all())

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups','experto','avistamiento',]
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class GrupoAnimalSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    """
    Serializador del modelo GrupoAnimal con el campo nombre_grupo_animal.
    """
    class Meta:
        model = Grupo_Animal
        fields = [
            'nombre_grupo_animal',
        ]


class FamiliaAnimalSerializer(UniqueFieldsMixin, NestedCreateMixin, NestedUpdateMixin, serializers.ModelSerializer):
    """
    Serializador del modelo FamiliaAnimal con los campos nombre_familia_animal y grupo_animal.
    Referencia a GrupoAnimalSerializer como campo foraneo.
    """
    grupo_animal = GrupoAnimalSerializer(allow_null=False)

    class Meta:
        model = Familia_Animal
        fields = [
            'nombre_familia_animal',
            'grupo_animal',
        ]
        depth = 1


class EspecieAnimalSerializer(UniqueFieldsMixin, NestedCreateMixin, NestedUpdateMixin, serializers.ModelSerializer):
    """
    Serializador del modelo EspecieAnimal con los campos nombre_especie_animal y familia_animal.
    Referencia a FamiliaAnimalSerializer como campo foraneo.
    """
    familia_animal = FamiliaAnimalSerializer(allow_null=False)

    class Meta:
        model = Especie_Animal
        fields = [
            'nombre_especie_animal',
            'familia_animal',
        ]
        depth = 1


class AnimalSerializer(NestedCreateMixin, serializers.ModelSerializer):
    """
        Serializador del modelo Animal con los campos nombre_local, estacionalidad y especie.
        Referencia a EspecieAnimalSerializer como campo foraneo.
    """
    especie = EspecieAnimalSerializer(allow_null=False)

    class Meta:
        model = Animal
        fields = [
            'nombre_local',
            'estacionalidad',
            'especie',
        ]
        depth = 1


class ExpertoSerializer(WritableNestedModelSerializer):
    """
    Serializador del modelo Experto con los campos id_experto, nombre_experto, apellido_experto, institucion_experto,
    identificacion_experto y usuario.
    Referencia a usuario como solo lectura y campo foraneo.
    """
    usuario = serializers.ReadOnlyField(source='usuario.username')

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
        read_only_fields = ('id_experto',)


class AvistamientoSerializer(WritableNestedModelSerializer):
    """
    Serializador del modelo Avistamiento con los campos id_avistamiento, geom, confirmado, fecha_hora,
    fotografia, descripcion, usuario y animal.
    Referencia a usuario como solo lectura y campo foraneo, se hace tambien referencia a animal como campo foraneo.
    """
    usuario = serializers.ReadOnlyField(source='usuario.username')
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
