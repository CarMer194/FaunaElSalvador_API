from django.forms import ModelForm

from API.models import Avistamiento


class AvistamientoForm(ModelForm):
    class Meta:
        model = Avistamiento
        fields = [
            'geom',
            'fotografia',
            'descripcion',
            'animal',
            'usuario',
            'fecha_hora',
        ]


