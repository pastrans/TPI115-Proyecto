from django.shortcuts import render, redirect
from apps.seccion.models import Seccion
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def resumenSeccion(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    secciones = Seccion.objects.filter(estado='A')
    if request.method == 'POST':
        secciones = Seccion.objects.filter(estado=request.POST['estado'])
    data = {'secciones' : secciones}
    return render(request, 'seccion/administrar.html', data)

@login_required
def agregarSeccion(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        nombre = request.POST['nombre']
        seccion = Seccion(nombre = nombre)
        seccion.save()
        return redirect('resumenSeccion')
    return redirect('resumenSeccion')

@login_required
def editarSeccion(request, idSeccion):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        seccion = Seccion.objects.get(idSeccion = idSeccion)
        seccion.nombre = request.POST['nombre']
        seccion.save()
        return redirect('resumenSeccion')
    return redirect('resumenSeccion')

@login_required
def eliminarSeccion(request, idSeccion):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    seccion = Seccion.objects.get(idSeccion = idSeccion)
    seccion.estado = 'I'
    seccion.save()
    return redirect('resumenSeccion')