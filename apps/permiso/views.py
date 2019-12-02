from django.shortcuts import render, redirect
from apps.permiso.models import Permiso
from apps.modulo.models import Modulo
from django.contrib.auth.decorators import login_required
import re

# Create your views here.

@login_required
def resumenPermiso(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    modulos = Modulo.objects.all()
    permisos = Permiso.objects.filter(estado = 'A')
    if request.method == 'POST':
        estado = request.POST['estado']
        permisos = Permiso.objects.filter(estado = estado)
    data = {'permisos' : permisos, 'modulos': modulos}
    return render(request, 'permiso/permiso.html', data)

@login_required
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

@login_required
def cambiarEstado(request,idPermiso,estado):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    permiso = Permiso.objects.get(idPermiso = idPermiso)
    permiso.estado = estado
    permiso.save()
    return redirect('resumenPermiso')

@login_required
def editarPermiso(request, idPermiso):
    permiso = Permiso.objects.get(idPermiso=idPermiso)
    modulos = Modulo.objects.all()
    permisos = Permiso.objects.filter(estado = 'A')
    if request.method == "POST":
        permiso.nombre = request.POST["nombrePermiso"]
        modulosPermiso = request.POST.getlist('modulos')
        permiso.modulo.clear()
        for modulo in modulosPermiso:
            modulo = Modulo.objects.get(idModulo=modulo)
            permiso.modulo.add(modulo) 
        permiso.save()
        return redirect('resumenPermiso')
    data = {'permiso' : permiso, 'modulos' : modulos, 'permisos' : permisos, 'editando': True}
    return render(request, 'permiso/permiso.html', data)