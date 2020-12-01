from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import AvistamientoForm
from API.models import Avistamiento


# Create your views here.

def formulario(request, point, user,date):
    mensaje = "¡Guardado con exito!"
    user_instance = User.objects.get(username=user)
    showmessage = False
    if request.method == 'POST':
        form = AvistamientoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            showmessage = True
    else:
        form = AvistamientoForm()
    context = {'form': form,
               'mensaje': mensaje,
               'point': point,
               'user': user_instance,
               'showmessage': showmessage,
               'date': date,
               }
    return render(request, 'Formulario.html', context)


def resultado(request):
    return render(request,'Resultado.html')