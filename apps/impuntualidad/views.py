from django.shortcuts import render, redirect
from django.db.models import Q
from apps.estudiante.models import Estudiante
from apps.impuntualidad.models import Impuntualidad
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def impuntualidadIndex(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Impuntualidad" in request.session['modulos']:
        return redirect('/index')
    data = {}
    impuntualidades = Impuntualidad.objects.filter(fecha=timezone.now())
    if request.method == 'POST':
        fecha = timezone.now()
        hora = datetime.datetime.now()
        if not 'horaServidor' in request.POST:
            hora = request.POST['hora']
        if not 'hoy' in request.POST:
            fecha = request.POST['fecha']
        impuntualidad = Impuntualidad(hora=hora, fecha=fecha, estudiante_id=request.POST['estudiante'])
        impuntualidad.save()
    estudiantes = Estudiante.objects.filter(estado='A').order_by('apellido')
    data = {'estudiantes' : estudiantes, 'hoy' : timezone.now(), 'impuntualidades' : impuntualidades}
    return render(request, 'impuntualidad/administrar.html', data)

@login_required
def buscar(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Impuntualidad" in request.session['modulos']:
        return redirect('/index')
    data = {}
    impuntualidades = {}
    if request.method == 'POST':
        campos = {}
        for key, value in request.POST.items():
            if key in ['estudiante_id', 'fecha']:
                campos[key] = value
        impuntualidades = Impuntualidad.objects.filter(**campos)
    estudiantes = Estudiante.objects.filter(estado='A').order_by('apellido')
    data = {'estudiantes' : estudiantes, 'hoy' : timezone.now(), 'impuntualidades' : impuntualidades}
    return render(request, 'impuntualidad/buscar.html', data)

@login_required
def eliminar(request, idImpuntualidad):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Impuntualidad" in request.session['modulos']:
        return redirect('/index')
    i = Impuntualidad.objects.get(idImpuntualidad=idImpuntualidad)
    i.delete()
    return redirect('indexImpuntualidad')