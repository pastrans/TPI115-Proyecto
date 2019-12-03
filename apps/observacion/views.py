from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from apps.observacion.models import Observacion
from apps.estudiante.models import Estudiante
from apps.personal.models import Personal

# Create your views here.

@login_required
def resumenObservacion(request):
    #Validación
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Observación" in request.session['modulos']:
        return redirect('/index')
    estudiantes = Estudiante.objects.all()
    personal = Personal.objects.get(idPersonal=request.session['id'])
    data = {'estudiantes' : estudiantes, 'personal' : personal}
    return render(request, 'observacion/observacion.html', data)

@login_required
def agregarObservacion(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Observación" in request.session['modulos']:
        return redirect('/index')
    if request.method == 'POST':
        personal_id = request.session['id']
        estudiante_id = request.POST['estudiante_id']
        fecha = timezone.now()
        observacion = request.POST['observacion']
        observacion = Observacion(observacion=observacion, fecha=fecha, personal_id=personal_id, estudiante_id=estudiante_id)
        observacion.save()
    return redirect(resumenObservacion)

@login_required
def amonestacionBuscar(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    data = {}
    amonestaciones = {}
    estudiante = {}
    estudiantes = Estudiante.objects.filter(estado='A').order_by('apellido')
    faltas = Falta.objects.filter(estado='A')
    tiposFalta = TipoFalta.objects.filter(estado='A')
    if request.method == 'POST':
        estudiante = Estudiante.objects.get(idEstudiante=request.POST['estudiante_id'])
        amonestaciones = Amonestacion.objects.filter(estudiante=estudiante)
    data = {'estudiantes' : estudiantes, 'amonestaciones' : amonestaciones, 'estudianteBuscar' : estudiante}
    return render(request, 'amonestacion/buscar.html', data)
