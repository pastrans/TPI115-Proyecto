from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from apps.observacion.models import Observacion
from apps.estudiante.models import Estudiante
from apps.personal.models import Personal

# Create your views here.

@login_required
def resumenObservacion(request):
    #Validación de permisos
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Observación" in request.session['modulos']:
        return redirect('/index')
    #Método
    estudiantes = Estudiante.objects.all()
    personal = Personal.objects.get(idPersonal=request.session['id'])
    data = {'estudiantes' : estudiantes, 'personal' : personal}
    return render(request, 'observacion/observacion.html', data)

@login_required
def agregarObservacion(request):
    #Validación de permisos
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Observación" in request.session['modulos']:
        return redirect('/index')
    #Método
    if request.method == 'POST':
        personal_id = request.session['id']
        estudiante_id = request.POST['estudiante_id']
        fecha = timezone.now()
        observacion = request.POST['observacion']
        observacion = Observacion(observacion=observacion, fecha=fecha, personal_id=personal_id, estudiante_id=estudiante_id)
        observacion.save()
    return redirect(resumenObservacion)

@login_required
def buscarObservacion(request):
    #Validación de permisos
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Observación" in request.session['modulos']:
        return redirect('/index')
    #Método
    estudiante = {}
    observaciones = {}
    estudiantes = Estudiante.objects.filter(estado='A').order_by('apellido')    
    if request.method == 'POST':
        estudiante = Estudiante.objects.get(idEstudiante=request.POST['estudiante_id'])
        observaciones = Observacion.objects.filter(estudiante=estudiante)
    data = {'estudiantes' : estudiantes, 'estudianteBuscar' : estudiante, 'observaciones' : observaciones}
    return render(request, 'observacion/buscar.html', data)

@login_required
def eliminarObservacion(request, idObservacion):
    #Validación de permisos
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Observación" in request.session['modulos']:
        return redirect('/index')
    #Método
    observacion = Observacion.objects.get(idObservacion=idObservacion)
    observacion.delete()
    return redirect('buscarObservacion')