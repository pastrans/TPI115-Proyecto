from django.shortcuts import render, redirect
from apps.sancion.models import Sancion
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
@login_required
def resumenSancion(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Sanción" in request.session['modulos']:
        return redirect('/index')
    page = request.GET.get('page', 1)
    sanciones_list = Sancion.objects.filter(estado='A')
    paginator = Paginator(sanciones_list, 5)
    sanciones = paginator.page(page)
    if request.method == 'POST':
        sanciones = Sancion.objects.filter(estado=request.POST['estado'])
    data = {'sanciones' : sanciones}
    return render(request, 'sancion/gestionarSancion.html', data)

@login_required
def agregarSancion(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Sanción" in request.session['modulos']:
        return redirect('/index')
    if request.method == 'POST':
        descripcion = request.POST['descripcion']
        sancion = Sancion(descripcion = descripcion)
        sancion.save()
        return redirect('resumenSancion')
    return redirect('resumenSancion')

@login_required
def editarSancion(request, idSancion):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Sanción" in request.session['modulos']:
        return redirect('/index')
    if request.method == 'POST':
        sancion = Sancion.objects.get(idSancion = idSancion)
        sancion.descripcion = request.POST['descripcion']
        sancion.save()
        return redirect('resumenSancion')
    return redirect('resumenSancion')

@login_required
def estadoSancion(request, idSancion, estado):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Sanción" in request.session['modulos']:
        return redirect('/index')
    sancion = Sancion.objects.get(idSancion = idSancion)
    sancion.estado = estado
    sancion.save()
    return redirect('resumenSancion')