from django.shortcuts import render, redirect
from apps.tiempo.models import Tiempo
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def resumenTiempo(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Tiempo" in request.session['modulos']:
        return redirect('/index')
    t = Tiempo.objects.filter(estado = 'A').order_by('horaInicial')
    if request.method == 'POST': #el post es para cambiar estado
        estado = request.POST['estado']
        t = Tiempo.objects.filter(estado = estado).order_by('horaInicial')
    data = {'tiempos' : t}
    return render(request, 'tiempo/tiempo.html', data)

@login_required
def agregarTiempo(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Tiempo" in request.session['modulos']:
        return redirect('/index')
    if request.method == 'POST':
        hIni = request.POST['horaI']
        hFin = request.POST['horaF']
        t = Tiempo(horaInicial = hIni, horaFinal = hFin, estado = 'A')
        t.save()
    return redirect('resumenTiempo')

@login_required
def editarTiempo(request,idTiempo):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Tiempo" in request.session['modulos']:
        return redirect('/index')
    if request.method == 'POST':
        t = Tiempo.objects.get(idTiempo = idTiempo)
        t.horaInicial = request.POST['horaI']
        t.horaFinal = request.POST['horaF']
        t.save()
    return redirect('resumenTiempo')

@login_required
def cambiarEstado(request,idTiempo,estado):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Tiempo" in request.session['modulos']:
        return redirect('/index')
    print(estado)
    print(idTiempo)
    t = Tiempo.objects.get(idTiempo = idTiempo)
    t.estado = estado
    t.save()
    return redirect('resumenTiempo')