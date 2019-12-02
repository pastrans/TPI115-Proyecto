from django.shortcuts import render, redirect
from apps.grado.models import Grado
from django.contrib.auth.decorators import login_required


# Create your views here.
# para mostrar los registros creamos la funcion resumenGrado
@login_required
def resumenGrado(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    grados = Grado.objects.filter(estado='A')
    if request.method == 'POST':
        grados = Grado.objects.filter(estado=request.POST['estado'])
    data = {'grados' : grados}
    return render(request, 'grado/administrar.html', data)


# para guardar un registro en la base de datos
@login_required
def agregarGrado(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nivel = request.POST['nivel']
        grado = Grado(nombre = nombre, nivel = nivel)
        grado.save()
        return redirect('resumenGrado')
    return redirect('resumenGrado')

# para editar un registro de grado
@login_required
def editarGrado(request, idGrado):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        grado = Grado.objects.get(idGrado = idGrado)
        grado.nombre = request.POST['nombre']
        grado.nivel = request.POST['nivel']
        grado.save()
        return redirect('resumenGrado')
    return redirect('resumenGrado')

# para eliminar un registro de grado (solo de cambia el estado para mantener la integridad de los datos)
@login_required
def estadoGrado(request, idGrado, estado):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    grado = Grado.objects.get(idGrado = idGrado)
    grado.estado = estado
    grado.save()
    return redirect('resumenGrado')
