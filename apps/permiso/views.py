from django.shortcuts import render, redirect
from apps.permiso.models import Permiso
from apps.modulo.models import Modulo
from django.contrib.auth.decorators import login_required
import re

# Create your views here.

@login_required
def resumenPermisoAntes(request):
    #permiso = Permiso.objects.get(idPermiso=request.session['id'])
    permisos = Permiso.objects.all()
    modulos = Modulo.objects.all()
    errores = set()
    if request.method == 'POST':
        errores = validarDatos(request.POST["nombre"])
        if len(errores) == 0:
            permiso = Permiso(nombre=request.POST["nombre"])
            permiso.save()
            modulosPermiso = request.POST.getlist('modulos')
            for modulo in modulosPermiso:
                modulo = Modulo.objects.get(idModulo=modulo)
                permiso.modulo.add(modulo)
            return redirect('resumenPermiso')
    data = {'permisos' : permisos, 'modulos': modulos,  'errores' : errores,
    'editando': False}
    return render(request, 'permiso/permiso.html', data)

#Funcionando
def resumenPermiso(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    permisos = Permiso.objects.filter(estado = 'A')
    if request.method == 'POST':
        estado = request.POST['estado']
        permisos = Permiso.objects.filter(estado = estado)
    data = {'permisos' : permisos}
    return render(request, 'permiso/permiso.html', data)

#Funcionando
def agregarPermiso(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        permiso = Permiso(nombre=request.POST["nombrePermiso"])
        permiso.save()
        modulosPermiso = request.POST.getlist('modulos')
        for modulo in modulosPermiso:
            modulo = Modulo.objects.get(idModulo=modulo)
            permiso.modulo.add(modulo)
    return redirect('resumenPermiso')

#Funcionando
def cambiarEstado(request,idPermiso,estado):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    permiso = Permiso.objects.get(idPermiso = idPermiso)
    permiso.estado = estado
    permiso.save()
    return redirect('resumenPermiso')

@login_required
def nuevoPermiso(request):
    data = {}
    errores = set()
    if request.method == 'POST':
        errores = validarDatosr(request.POST["nombre"])
        if len(errores) == 0:
            permiso = Permiso(nombre=request.POST["nombre"])
            permiso.save()
            modulosPermiso = request.POST.getlist('modulos')
            for modulo in modulosPermiso:
                modulo = Modulo.objects.get(idModulo=modulo)
                permiso.modulo.add(modulo)
    data = {'errores' : errores}
    return render(request, 'permiso/permiso.html', data)

@login_required
def editarPermiso(request, idPermiso):
    permiso = Permiso.objects.get(idPermiso=idPermiso)
    modulos = Modulo.objects.all()
    data = {'permiso' : permiso, 'modulos' : modulos, 'editando': True}
    errores = set()
    if request.method == 'POST':
        errores = validarDatos(request.POST["nombre"])
        if len(errores) == 0:
            permiso.nombre = request.POST["nombre"]
            permiso.save()
            permiso.modulo.clear()
            modulosPermiso = request.POST.getlist('modulos')
            for modulo in modulosPermiso:
                modulo = Modulo.objects.get(idModulo=modulo)
                permiso.modulo.add(modulo)
            return redirect('resumenPermiso')
        else:
            data = {'permiso' : permiso, 'modulos' : modulos,
            'errores' : errores, 'editando': True}
    return render(request, 'permiso/permiso.html', data)

@login_required
def eliminarPermiso(request, idPermiso):
    permiso = Permiso.objects.get(idPermiso=idPermiso)
    permiso.delete()
    return redirect('resumenPermiso')

def validarDatos(nombre):
    errores = set()
    if(not re.match("^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ0-9 ]+$", nombre)):
        errores.add('Nombre inválido')
    return errores
