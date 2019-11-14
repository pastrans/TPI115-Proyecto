from django.shortcuts import render, redirect
from apps.seccion.models import Seccion

# Create your views here.
def resumenSeccion(request):
    secciones = Seccion.objects.filter(estado='A')
    if request.method == 'POST':
        secciones = Seccion.objects.filter(estado=request.POST['estado'])
    data = {'secciones' : secciones}
    return render(request, 'seccion/administrar.html', data)

def agregarSeccion(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        seccion = Seccion(nombre = nombre)
        seccion.save()
        return redirect('resumenSeccion')
    return redirect('resumenSeccion')

def editarSeccion(request, idSeccion):
    if request.method == 'POST':
        seccion = Seccion.objects.get(idSeccion = idSeccion)
        seccion.nombre = request.POST['nombre']
        seccion.save()
        return redirect('resumenSeccion')
    return redirect('resumenSeccion')

def eliminarSeccion(request, idSeccion):
    seccion = Seccion.objects.get(idSeccion = idSeccion)
    seccion.estado = 'I'
    seccion.save()
    return redirect('resumenSeccion')