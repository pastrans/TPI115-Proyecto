from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.estudiante.models import Estudiante
from apps.usuario.models import Usuario
from apps.permiso.models import Permiso
from apps.seccionGrado.models import SeccionGrado


# Create your views here.

@login_required
def resumenPersonal(request):
    #Validación de permisos
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if not "Estudiante" in request.session['modulos']:
        return redirect('/index')
    #Método    
    estudiantes = Estudiante.objects.filter(estado = 'A')
    seccionGrados = SeccionGrado.objects.all()
    if request.method == 'POST': #el post es para cambiar estado
        estado = request.POST['estado']
        e = Estudiante.objects.filter(estado = estado)
    per = Permiso.objects.filter(estado = 'A')
    usus = []
    for ps in p:
        u = Usuario.objects.filter(personal = ps)
        if u.exists():
            usus.append(u[0])
        else:
            usus.append('') #esto nunca deberia ocurrir
    cross = zip(p,usus)
    data = {'estudiantes' : estudiantes, 'seccionGrados' : seccionGrados, 'permisos' : per, 'cross' : cross}
    return render(request, 'estudiante/estudiante.html', data)

@login_required
def agregarPersonal(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        codigo = request.POST['codigoP']
        nombre = request.POST['nombreP']
        apellido = request.POST['apellidoP']
        #usuario
        clave = request.POST['claveP']
        perm = Permiso.objects.get(idPermiso = request.POST['permisoP'])
        Per = Personal(codigo = codigo, nombre = nombre, apellido = apellido, estado = 'A')
        U = Usuario(codigo = codigo, personal = Per, permiso = perm)
        U.set_password(clave)        
        Per.save()
        U.save()
        return redirect('resumenPersonal')
    return redirect('resumenPersonal')

@login_required
def editarPersonal(request, idPnal):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':        
        perE = Personal.objects.get(idPersonal = idPnal)        
        perE.nombre = request.POST['nombreP']
        perE.codigo = request.POST['codigoP']
        perE.apellido = request.POST['apellidoP']
        perE.save()
        #usuario
        permi = Permiso.objects.get(idPermiso = request.POST['permisoP'])
        nuevaPass = request.POST.getlist('chkCambiar')       
        u = Usuario.objects.get(personal = perE)
        u.codigo = request.POST['codigoP']
        u.permiso = permi
        for s in nuevaPass:            
            if s == '1':
                clave = request.POST['claveP']
                u.set_password(clave)
        u.save()
        return redirect('resumenPersonal')
    return redirect('resumenPersonal')

@login_required
def cambiarEstado(request,idPnal,estado):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    perE = Personal.objects.get(idPersonal = idPnal)
    perE.estado = estado
    perE.save() 
    #cambiar estado de usuario
    Usu = Usuario.objects.get(personal = perE)
    Usu.estado = estado
    Usu.save()
    return redirect('resumenPersonal')