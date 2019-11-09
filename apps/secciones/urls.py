from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required
from apps.secciones.views import inicio
urlpatterns = [
    url(r'^$', login_required(inicio), name='inicio'),
]
