from django.shortcuts import render, redirect
from apps.tipoFalta.models import TipoFalta
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def resumenTipoFalta(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    tipos = TipoFalta.objects.filter(estado='A')
    if request.method == 'POST':
    	tipos = TipoFalta.objects.filter(estado=request.POST['estado'])
       
    data = {'tipos' : tipos}
    return render(request, 'tipoFalta/gestionarTipoFalta.html', data)

@login_required
def agregarTipoFalta(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        nombre = request.POST['nombre']
        tipoFalta = TipoFalta(nombre = nombre)
        tipoFalta.save()
        return redirect('resumenTipoFalta')
    return redirect('resumenTipoFalta')

@login_required
def editarTipoFalta(request, idTipo):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        tipoFalta = TipoFalta.objects.get(idTipoFalta = idTipo)
        tipoFalta.nombre = request.POST['nombre']
        tipoFalta.save()
        return redirect('resumenTipoFalta')
    return redirect('resumenTipoFalta')

@login_required
def estadoTipoFalta(request, idTipo, estado):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    tipoFalta =TipoFalta.objects.get(idTipoFalta = idTipo)
    tipoFalta.estado = estado
    tipoFalta.save()
    return redirect('resumenTipoFalta')