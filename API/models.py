from django.contrib.gis.db import models
from django.conf import settings
# Create your models here.
"""Clases con los modelos a implementar en la base de datos"""


class Grupo_Animal(models.Model):
    """Modelo que representa al grupo biologico del animal"""
    nombre_grupo_animal = models.CharField(max_length=500, primary_key=True)

    def __str__(self):
        return self.nombre_grupo_animal


class Familia_Animal(models.Model):
    """Modelo que representa a la familia biologica del animal"""
    nombre_familia_animal= models.CharField(max_length=500, primary_key=True)
    grupo_animal = models.ForeignKey(Grupo_Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_familia_animal


class Especie_Animal(models.Model):
    """Modelo que representa a la especie bologica del animal"""
    nombre_especie_animal = models.CharField(max_length=500, primary_key=True)
    familia_animal = models.ForeignKey(Familia_Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_especie_animal


class Animal(models.Model):
    """Modelo que representa al animal, con su nombre local de El Salvador"""
    nombre_local = models.CharField(max_length=600, primary_key=True)
    estacionalidad = models.CharField(max_length=400)
    especie = models.ForeignKey(Especie_Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_local


class Experto(models.Model):
    """Modelo que representa los datos de un usuario experto en biologia que le da el
    acceso a verificar avistamientos"""
    id_experto = models.AutoField(primary_key=True)
    nombre_experto = models.CharField(max_length=200)
    apellido_experto = models.CharField(max_length=200)
    institucion_experto = models.CharField(max_length=300)
    identificacion_experto = models.CharField(max_length=500)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_experto + ' ' + self.apellido_experto + '.'


class Avistamiento(models.Model):
    """Modelo que representa un avistamiento de un animal, el campo geom es un modelo espacial vector punto"""
    id_avistamiento = models.AutoField(primary_key=True)
    geom = models.GeometryField()
    confirmado = models.BooleanField(default=False)
    fecha_hora = models.DateTimeField(blank=True, null=True)
    fotografia = models.ImageField()
    descripcion = models.TextField(max_length=1000, blank=True, null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.__str__() + ' , ' + self.animal.__str__() \
               + ' ' + self.fecha_hora.__str__() + '.'
