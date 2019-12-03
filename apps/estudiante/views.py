from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.estudiante.models import Estudiante
from apps.usuario.models import Usuario
from apps.permiso.models import Permiso
from apps.seccionGrado.models import SeccionGrado

import random

# Create your views here.

@login_required
def resumenEstudiante(request):
    #Validación de permisos
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Estudiante" in request.session['modulos']:
        return redirect('/index')
    #Método    
    estudiantes = Estudiante.objects.filter(estado = 'A')
    seccionGrados = SeccionGrado.objects.all()
    if request.method == 'POST': #el post es para cambiar estado
        estado = request.POST['estado']
        estudiantes = Estudiante.objects.filter(estado = estado)
    data = {'estudiantes' : estudiantes, 'seccionGrados' : seccionGrados}
    return render(request, 'estudiante/estudiante.html', data)

@login_required
def agregarEstudiante(request):
    #Validación de permisos
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Estudiante" in request.session['modulos']:
        return redirect('/index')
    #Método 
    if request.method == 'POST':
        codigo = request.POST['codigoEstudiante']
        nombre = request.POST['nombreEstudiante']
        apellido = request.POST['apellidoEstudiante']
        seccionGrado_id = request.POST['seccionGrado_id']
        #usuario
        clave = request.POST['claveEstudiante']
        estudiante = Estudiante(codigo = codigo, nombre = nombre, apellido = apellido, seccionGrado_id=seccionGrado_id, estado = 'A')
        usuario = Usuario(codigo = codigo, estudiante = estudiante)
        usuario.set_password(clave)        
        estudiante.save()
        usuario.save()
    return redirect('resumenEstudiante')

@login_required
def editarEstudiante(request, idEstudiante):
    #Validación de permisos
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Estudiante" in request.session['modulos']:
        return redirect('/index')
    #Método 
    if request.method == 'POST':        
        estudiante = Estudiante.objects.get(idEstudiante = idEstudiante)        
        estudiante.nombre = request.POST['nombreEstudiante']
        estudiante.codigo = request.POST['codigoEstudiante']
        estudiante.apellido = request.POST['apellidoEstudiante']
        estudiante.seccionGrado_id = request.POST['seccionGrado_id']
        estudiante.save()
        #usuario
        #permi = Permiso.objects.get(idPermiso = request.POST['permisoP'])
        nuevaPass = request.POST.getlist('chkCambiar')       
        #u = Usuario.objects.get(personal = perE)
        u.codigo = request.POST['codigoP']
        u.permiso = permi
        for s in nuevaPass:            
            if s == '1':
                clave = request.POST['claveP']
                u.set_password(clave)
        u.save()
        return redirect('resumenEstudiante')
    return redirect('resumenEstudiante')

@login_required
def cambiarEstado(request, idEstudiante, estado):
    #Validación de permisos
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Estudiante" in request.session['modulos']:
        return redirect('/index')
    #Método 
    estudiante = Estudiante.objects.get(idEstudiante = idEstudiante)
    estudiante.estado = estado
    estudiante.save() 
    #cambiar estado de usuario
    #usuario = Usuario.objects.get(estudiante = estudiante)
    #usuario.estado = estado
    #usuario.save()
    return redirect('resumenEstudiante')