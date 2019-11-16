"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
#from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #path('secciones/', include('apps.secciones.urls')),
    path('', include('apps.login.urls'), name='sesion'),
    path('index/', include('apps.index.urls'), name='index'),
    path('my/', include('apps.public.urls'), name='myindex'),
    path('seccion/', include('apps.seccion.urls'), name="seccion"),
    path('amonestacion/', include('apps.amonestacion.urls'), name="amonestacion"),
    path('asignatura/', include('apps.asignatura.urls'), name="asignatura"),
    path('especialidad/', include('apps.especialidad.urls'), name="especialidad"),
    path('estudiante/', include('apps.estudiante.urls'), name="estudiante"),
    path('falta/', include('apps.falta.urls'), name="falta"),
    path('grado/', include('apps.grado.urls'), name="grado"),
    path('horaClase/', include('apps.horaClase.urls'), name="horaClase"),
    path('impuntualidad/', include('apps.impuntualidad.urls'), name="impuntualidad"),
    path('inasistencia/', include('apps.inasistencia.urls'), name="inasistencia"),
    path('observacion/', include('apps.observacion.urls'), name="observacion"),
    path('permiso/', include('apps.permiso.urls'), name="permiso"),
    path('personal/', include('apps.personal.urls'), name="personal"),
    path('sancion/', include('apps.sancion.urls'), name="sancion"),
    path('seccionGrado/', include('apps.seccionGrado.urls'), name="seccionGrado"),
    path('tiempo/', include('apps.tiempo.urls'), name="tiempo"),
    path('tipoFalta/', include('apps.tipoFalta.urls'), name="tipoFalta"),
    #url(r'^admin/', admin.site.urls),
]
