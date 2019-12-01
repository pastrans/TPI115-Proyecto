from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from apps.estudiante.models import Estudiante
from apps.inasistencia.models import Inasistencia, AsistenciaGrado
from apps.seccionGrado.models import SeccionGrado
from django.contrib.auth.decorators import login_required

import datetime
import csv, io, os, re

os.environ['TZ'] = 'America/El_Salvador'

@login_required
def administrarAsistencia(request):
    gradosListados = AsistenciaGrado.objects.filter(fecha=datetime.date.today()).values('seccionGrado_id')
    gl = set()
    for gradoListado in gradosListados:
        gl.add(gradoListado['seccionGrado_id'])
    grados = SeccionGrado.objects.filter(grado__estado='A', seccion__estado='A')
    data = {'gradosListados' : gl, 'grados' : grados}
    return render(request, 'asistencia/administrar.html', data)

@login_required
def asistenciaDiferida(request, idSeccionGrado, fecha):
    seccionGrado = SeccionGrado.objects.get(idSeccionGrado=idSeccionGrado)
    estudiantes = Estudiante.objects.filter(seccionGrado_id=idSeccionGrado, estado='A').order_by('apellido')
    d = fecha[0:2]
    m = fecha[2:4]
    a = fecha[4:]
    fechaDiferida = a + "-" + m + "-" + d
    inasistencias = set()
    asistenciaGrado = False
    if request.method == 'POST':
        if AsistenciaGrado.objects.filter(seccionGrado_id=idSeccionGrado, fecha=fechaDiferida).count() == 0:
            a = AsistenciaGrado(seccionGrado_id=idSeccionGrado, fecha=fechaDiferida)
            a.save()
            asistenciaGrado = True
        estudiantesIDs = list(map(int, request.POST.getlist('asistencias')))
        for estudiante in estudiantes:
            if not estudiante.idEstudiante in estudiantesIDs:
                if Inasistencia.objects.filter(estudiante=estudiante, fecha=fechaDiferida).count() == 0:
                    i = Inasistencia(estudiante=estudiante, fecha=fechaDiferida)
                    i.save()
                    inasistencias.add(estudiante.codigo)
            elif Inasistencia.objects.filter(estudiante=estudiante, fecha=fechaDiferida).count() == 1:
                i = Inasistencia.objects.filter(estudiante=estudiante, fecha=fechaDiferida)
                i.delete()
    if Inasistencia.objects.filter(estudiante__seccionGrado_id=idSeccionGrado, fecha=fechaDiferida).count() == 0 and AsistenciaGrado.objects.filter(seccionGrado_id=idSeccionGrado, fecha=fechaDiferida).count() == 0:
        asistenciaGrado = False
        for estudiante in estudiantes:
            inasistencias.add(estudiante.codigo)
    else:
        inasistenciasData = Inasistencia.objects.filter(fecha=fechaDiferida)
        for fila in inasistenciasData:
            inasistencias.add(fila.estudiante.codigo)
    data = {'estudiantes' : estudiantes, 'inasistencias' : inasistencias, 'asistenciaGrado' : asistenciaGrado, 'seccionGrado' : seccionGrado, 'fecha': fechaDiferida}
    return render(request, 'asistencia/asistencia.html', data)

@login_required
def pasarAsistencia(request, idSeccionGrado):
    seccionGrado = SeccionGrado.objects.get(idSeccionGrado=idSeccionGrado)
    estudiantes = Estudiante.objects.filter(seccionGrado_id=idSeccionGrado, estado='A').order_by('apellido')
    inasistencias = set()
    asistenciaGrado = False
    comprobar = ""
    if request.method == 'POST':
        if AsistenciaGrado.objects.filter(seccionGrado_id=idSeccionGrado, fecha=datetime.date.today()).count() == 0:
            a = AsistenciaGrado(seccionGrado_id=idSeccionGrado, fecha=datetime.date.today())
            a.save()
            asistenciaGrado = True
        estudiantesIDs = list(map(int, request.POST.getlist('asistencias')))
        for estudiante in estudiantes:
            if not estudiante.idEstudiante in estudiantesIDs:
                if Inasistencia.objects.filter(estudiante=estudiante, fecha=datetime.date.today()).count() == 0:
                    i = Inasistencia(estudiante=estudiante)
                    i.save()
                    inasistencias.add(estudiante.codigo)
            elif Inasistencia.objects.filter(estudiante=estudiante, fecha=datetime.date.today()).count() == 1:
                i = Inasistencia.objects.filter(estudiante=estudiante, fecha=datetime.date.today())
                i.delete()
    if Inasistencia.objects.filter(estudiante__seccionGrado_id=idSeccionGrado, fecha=datetime.date.today()).count() == 0 and AsistenciaGrado.objects.filter(seccionGrado_id=idSeccionGrado, fecha=datetime.date.today()).count() == 0:
        asistenciaGrado = False
        for estudiante in estudiantes:
            inasistencias.add(estudiante.codigo)
    else:
        inasistenciasData = Inasistencia.objects.filter(fecha=datetime.date.today())
        for fila in inasistenciasData:
            inasistencias.add(fila.estudiante.codigo)
    data = {'estudiantes' : estudiantes, 'inasistencias' : inasistencias, 'asistenciaGrado' : asistenciaGrado, 'seccionGrado' : seccionGrado}
    return render(request, 'asistencia/asistencia.html', data)

def justificarView(request):
    estudiantes = Estudiante.objects.filter(estado='A').order_by('apellido')
    inasistencias = {}
    estudianteBuscar = {}
    if request.method == 'POST':
        inasistencias = Inasistencia.objects.filter(estudiante_id=request.POST['estudiante_id'])
        estudianteBuscar = Estudiante.objects.get(idEstudiante=request.POST['estudiante_id'])
    data = {'estudiantes' : estudiantes, 'inasistencias' : inasistencias, 'estudianteBuscar': estudianteBuscar}
    return render(request, 'asistencia/justificar.html', data)

def justificar(request, idInasistencia):
    
    i = Inasistencia.objects.get(idInasistencia=idInasistencia)
    i.estado = 'J'
    i.save()
    return HttpResponseRedirect(reverse('justificarView'))

def importCsv(request, fecha):
    f = fecha
    estudiantes = set()
    if request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return render(request, 'asistencia/csv.html', {"error" : "NO ES POSIBLE ABRIR EL ARCHIVO"})
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            alumno = Estudiante(
                nombre = column[1],
                apellido = column[0],
                codigo = column[2]
            )
            alumno.save()
            estudiantes.add(column[2])
    context = {'estudiantes' : estudiantes, 'fecha' : f}
    return render(request, 'asistencia/csv.html', context)