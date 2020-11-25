from django.contrib.auth.models import User
from rest_framework import serializers, generics
from .models import *
from drf_writable_nested.serializers import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):
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
