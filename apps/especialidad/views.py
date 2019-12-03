from django.shortcuts import render, redirect
from apps.especialidad.models import Especialidad
from django.contrib.auth.decorators import login_required 

@login_required
def resumenEspecialidad(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Especialidad" in request.session['modulos']:
        return redirect('/index')
    especialidad = Especialidad.objects.filter(estado='A')
    if request.method == 'POST':
        e = Especialidad()
        e.nombre= request.POST['nombre']
        e.save()
        return redirect('agregarEspecialidad')
        #e1 = request.POST.get('estado')
        # especialidad = Especialidad.objects.filter(estado=e1)
    data = {'especialidad':especialidad}
    return render(request, 'especialidad/administrar.html', data)

@login_required
def editarEspecialidad(request, idEspecialidad):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Especialidad" in request.session['modulos']:
        return redirect('/index')
    if request.method == 'POST':
        especialidad = Especialidad.objects.get(idEspecialidad = idEspecialidad)
        especialidad.nombre = request.POST['nombre']
        especialidad.save()
        return redirect('agregarEspecialidad')
    return redirect('agregarEspecialidad')

@login_required
def estadoEspecialidad(request, idEspecialidad, estado):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Especialidad" in request.session['modulos']:
        return redirect('/index')
    especialidad = Especialidad.objects.get(idEspecialidad = idEspecialidad)
    especialidad.estado = estado
    especialidad.save()
    return redirect('agregarEspecialidad')


# Create your views here.
