"""FaunaElSalvador_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from API import views

router = routers.DefaultRouter()
router.register(r'grupoanimal', views.GrupoAnimalView)
router.register(r'familiaanimal',views.FamiliaAnimalView)
router.register(r'especieanimal',views.EspecieAnimalView)
router.register(r'animal',views.AnimalView)
router.register(r'expertos',views.ExpertoView)
router.register(r'avistamientos',views.AvistamientoView)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path(r'users',views.UserList.as_view()),
    path(r'users/<int:pk>/',views.UserDetail.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]