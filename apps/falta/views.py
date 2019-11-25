from django.shortcuts import render, redirect
from apps.falta.models import Falta
from apps.tipoFalta.models import TipoFalta
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def resumenFalta(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    faltas = Falta.objects.filter(estado='A')
    tipos = TipoFalta.objects.filter(estado='A')
    if request.method == 'POST':
    	 faltas = Falta.objects.filter(estado=request.POST['estado'])
    data = {'faltas' : faltas, 'tipos': tipos,}
    return render(request, 'falta/gestionarFalta.html', data)

@login_required
def agregarFalta(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        descripcion = request.POST['descripcion']
        nomTipo = request.POST['tipo']
        tipo = TipoFalta.objects.get(nombre=nomTipo)
        falta = Falta(descripcion = descripcion, tipoFalta_id=tipo.idTipoFalta)
        falta.save()
        return redirect('resumenFalta')
    return redirect('resumenFalta')

@login_required
def editarFalta(request, idFalta):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        falta = Falta.objects.get(idFalta = idFalta)
        falta.descripcion = request.POST['descripcion']
        nomTipo = request.POST['tipo']
        tipo = TipoFalta.objects.get(nombre=nomTipo)
        falta.tipoFalta_id= tipo.idTipoFalta
        falta.save()
        return redirect('resumenFalta')
    return redirect('resumenFalta')

@login_required
def estadoFalta(request, idFalta, estado):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    falta = Falta.objects.get(idFalta = idFalta)
    falta.estado = estado
    falta.save()
    return redirect('resumenFalta')