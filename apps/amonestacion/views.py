from django.shortcuts import render, redirect
from django.http import JsonResponse
from apps.estudiante.models import Estudiante
from apps.falta.models import Falta
from apps.tipoFalta.models import TipoFalta
from apps.personal.models import Personal
from apps.amonestacion.models import Amonestacion
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
@login_required
def amonestacionIndex(request):
    data = {}
    estudiantes = Estudiante.objects.filter(estado='A').order_by('apellido')
    faltas = Falta.objects.filter(estado='A')
    tiposFalta = TipoFalta.objects.filter(estado='A')
    if request.method == 'POST':
        personal = Personal.objects.get(idPersonal=request.session['id'])
        campos = {'personal_id' : personal.idPersonal, 'fecha' : datetime.date.today()}
        for key, value in request.POST.items():
            if key in ['estudiante_id', 'falta_id', 'sancion_id']:
                campos[key] = value
        amonestacion = Amonestacion(**campos)
        amonestacion.save()
    data = {'estudiantes' : estudiantes, 'faltas' : faltas, 'tiposFalta' : tiposFalta}
    return render(request, 'amonestacion/amonestacion.html', data)

@login_required
def amonestacionBuscar(request):
    data = {}
    amonestaciones = {}
    estudiante = {}
    estudiantes = Estudiante.objects.filter(estado='A').order_by('apellido')
    faltas = Falta.objects.filter(estado='A')
    tiposFalta = TipoFalta.objects.filter(estado='A')
    if request.method == 'POST':
        estudiante = Estudiante.objects.get(idEstudiante=request.POST['estudiante_id'])
        amonestaciones = Amonestacion.objects.filter(estudiante=estudiante)
    data = {'estudiantes' : estudiantes, 'amonestaciones' : amonestaciones, 'estudiante' : estudiante}
    return render(request, 'amonestacion/buscar.html', data)

def amonestacionEliminar(request, idAmonestacion):
    a = Amonestacion.objects.get(idAmonestacion=idAmonestacion)
    a.delete()
    return redirect('amonestacionBuscar')