from django.shortcuts import render, redirect
from apps.personal.models import Personal

# Create your views here.

def resumenPersonal(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    p = Personal.objects.filter(estado = 'A')
    if request.method == 'POST': #el post es para cambiar estado
        estado = request.POST['estado']
        p = Personal.objects.filter(estado = estado)
    data = {'personal' : p}
    return render(request, 'personal/personal.html', data)

def agregarPersonal(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        codigo = request.POST['codigoP']
        nombre = request.POST['nombreP']
        apellido = request.POST['apellidoP']
        Per = Personal(codigo = codigo, nombre = nombre, apellido = apellido, estado = 'A')
        Per.save()
        return redirect('resumenPersonal')
    return redirect('resumenPersonal')

def editarPersonal(request, idPnal):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':        
        perE = Personal.objects.get(idPersonal = idPnal)
        perE.nombre = request.POST['nombreP']
        perE.codigo = request.POST['codigoP']
        perE.apellido = request.POST['apellidoP']
        perE.save()
        return redirect('resumenPersonal')
    return redirect('resumenPersonal')

def cambiarEstado(request,idPnal,estado):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    perE = Personal.objects.get(idPersonal = idPnal)
    perE.estado = estado
    perE.save() 
    #cambiar estado de usuario?
    return redirect('resumenPersonal')