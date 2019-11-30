from django.shortcuts import render, redirect
from apps.asignatura.models import Asignatura
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def resumenAsignatura(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    asignaturas = Asignatura.objects.filter(estado='A')
    if request.method == 'POST':
        asignaturas = Asignatura.objects.filter(estado=request.POST['estado'])
    data = {'asignaturas' : asignaturas}
    return render(request, 'asignatura/gestionarAsignatura.html', data)

@login_required
def agregarAsignatura(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        nombre = request.POST['nombre']
        asignatura = Asignatura(nombre = nombre)
        asignatura.save()
        return redirect('resumenAsignatura')
    return redirect('resumenAsignatura')

@login_required
def editarAsignatura(request, idAsignatura):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        asignatura = Asignatura.objects.get(idAsignatura = idAsignatura)
        asignatura.nombre = request.POST['nombre']
        asignatura.save()
        return redirect('resumenAsignatura')
    return redirect('resumenAsignatura')

@login_required
def estadoAsignatura(request, idAsignatura, estado):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    asignatura = Asignatura.objects.get(idAsignatura = idAsignatura)
    asignatura.estado = estado
    asignatura.save()
    return redirect('resumenAsignatura')