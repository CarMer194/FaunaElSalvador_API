from django.contrib import admin
from .models import *
# Register your models here.
"""Modelos a implementar en panel de administración"""
admin.site.register(Animal)
admin.site.register(Avistamiento)
admin.site.register(Especie_Animal)
admin.site.register(Grupo_Animal)
admin.site.register(Familia_Animal)
admin.site.register(Experto)
