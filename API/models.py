from django.contrib.gis.db import models
# Create your models here.

class Grupo_Animal(models.Model):
    idGrupo = models.AutoField(primary_key=True)
    nombre_grupo_animal = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre_grupo_animal


class Familia_Animal(models.Model):
    id_familia_animal = models.AutoField(primary_key=True)
    nombre_familia_animal= models.CharField(max_length=500)
    grupo_animal = models.ForeignKey(Grupo_Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_familia_animal


class Especie_Animal(models.Model):
    id_especie_animal = models.AutoField(primary_key=True)
    nombre_especie_animal = models.CharField(max_length=500)
    familia_animal = models.ForeignKey(Familia_Animal,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_especie_animal


class Animal(models.Model):
    id_Animal = models.AutoField(primary_key=True)
    nombre_local = models.CharField(max_length=600)
    estacionalidad = models.CharField(max_length=400)
    especie = models.ForeignKey(Especie_Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_local


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    correo_electronico = models.CharField(max_length=300)
    contrasenia = models.CharField(max_length=100)
    nombre_usuario = models.CharField(max_length=100)


class Experto(models.Model):
    id_experto = models.AutoField(primary_key=True)
    nombre_experto = models.CharField(max_length=200)
    apellido_experto = models.CharField(max_length=200)
    institucion_experto = models.CharField(max_length=300)
    identificacion_experto = models.CharField(max_length=500)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_experto + ' ' + self.apellido_experto + '.'


class Avistamiento(models.Model):
    id_avistamiento = models.AutoField(primary_key=True)
    geom = models.GeometryField()
    confirmado = models.BooleanField(default=False)
    fecha_hora = models.DateTimeField(blank=True, null=True)
    fotografia = models.ImageField()
    descripcion = models.TextField(max_length=1000, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.__str__() + ' , ' + self.animal.__str__() \
               + ' ' + self.fecha_hora + '.'
