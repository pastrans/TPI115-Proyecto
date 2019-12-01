from django.shortcuts import render, redirect
from django.http import JsonResponse
from apps.estudiante.models import Estudiante
from apps.falta.models import Falta
from apps.tipoFalta.models import TipoFalta
from apps.personal.models import Personal
from apps.amonestacion.models import Amonestacion
from apps.sancion.models import Sancion
from django.contrib.auth.decorators import login_required
import datetime, re
# Create your views here.
@login_required
def amonestacionIndex(request):
    data = {}
    errores = set()
    estudiantes = Estudiante.objects.filter(estado='A').order_by('apellido')
    faltas = Falta.objects.filter(estado='A')
    tiposFalta = TipoFalta.objects.filter(estado='A')
    sanciones = Sancion.objects.filter(estado='A')
    if request.method == 'POST':
        errores = validar(request.POST.get("falta_id", ""), request.POST.get("sancion_id", ""), request.POST.get("estudiante_id", ""))
        #errores = validar(request.POST['falta_id'], request.POST['sancion_id'], request.POST['estudiante_id'], request.POST['tipoFalta_id'])
        if len(errores) == 0:
            personal = Personal.objects.get(idPersonal=request.session['id'])
            campos = {'personal_id' : personal.idPersonal, 'fecha' : datetime.date.today()}
            for key, value in request.POST.items():
                if key in ['estudiante_id', 'falta_id', 'sancion_id']:
                    campos[key] = value
            amonestacion = Amonestacion(**campos)
            amonestacion.save()
    data = {'estudiantes' : estudiantes, 'faltas' : faltas, 'tiposFalta' : tiposFalta, 'sanciones' : sanciones, 'errores' : errores}
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
    data = {'estudiantes' : estudiantes, 'amonestaciones' : amonestaciones, 'estudianteBuscar' : estudiante}
    return render(request, 'amonestacion/buscar.html', data)

def amonestacionEliminar(request, idAmonestacion):
    a = Amonestacion.objects.get(idAmonestacion=idAmonestacion)
    a.delete()
    return redirect('amonestacionBuscar')

def validar(falta, sancion, estudiante):
    errores = set()
    if (not re.match("^[1-9]\d*$", falta)) or falta == "":
        errores.add("Falta no válida")
    if (not re.match("^[0-9]\d*$", sancion)) and sancion is not "":
        errores.add("Sanción no válida")
        errores.add("asdhjsa " + sancion)
    if (not re.match("^[1-9]*$", estudiante)) or estudiante == "":
        errores.add("Estudiante no válido")
    """if (not re.match("^[0-9]*$", tipoFalta)) or int(tipoFalta) == 0 or tipoFalta == "":
        errores.add("Tipo de falta no válida")
    faltasP = Faltas.objects.filter(tipoFalta_id=tipoFalta)
    if not falta in faltasP:
        errores.add("Falta no correspondiente a su tipo")"""
    return errores