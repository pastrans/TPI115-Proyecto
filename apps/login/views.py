from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as dj_login
from apps.usuario.models import Usuario
from apps.permiso.models import Permiso
from apps.estudiante.models import Estudiante
from apps.personal.models import Personal

# Create your views here.
def login(request):
    errores = set()
    data = {}
    if request.method == 'POST':
        codigo = request.POST['codigo']
        password = request.POST['password']
        usuario = authenticate(request, codigo=codigo, password=password)
        permiso = {}
        modulos = set()
        if usuario is not None:
            dj_login(request, usuario)
            user  = Usuario.objects.get(codigo=codigo)
            if user.personal_id is not None:
                personal = Personal.objects.get(codigo=codigo)
                request.session['id'] = personal.idPersonal
                request.session['nombre'] = personal.nombre + personal.apellido
                request.session['tipo'] = 'P'
            elif user.estudiante_id is not None:
                estudiante = Estudiante.objects.get(codigo=codigo)
                request.session['id'] = estudiante.idEstudiante
                request.session['nombre'] = estudiante.nombre + estudiante.apellido
                request.session['tipo'] = 'E'
            if user.permiso_id is not None:
                permiso = Permiso.objects.get(idPermiso=user.permiso_id)
                for modulo in permiso.modulo.all():
                    modulos.add(modulo.nombre)
            request.session['codigo'] = user.codigo
            request.session['permiso'] = user.permiso_id
            request.session['modulos'] = list(modulos)
            if user.personal_id is not None:
                return redirect('/index/')
            elif user.estudiante_id is not None:
                return redirect('/my/')
        else:
            errores.add('Usuario no encontrado')
            data = {'errores' : errores}
            return render(request, 'login/login.html', data)
    if 'id' in request.session:
        if request.session['tipo'] == 'P':
            return redirect('/index/')
        elif request.session['tipo'] == 'E':
            return redirect('/my/')
    return render(request, 'login/login.html', data)

def logoutView(request):
    if request.session.get('id'):
        del request.session['id']
    if request.session.get('nombre'):
        del request.session['nombre']
    if request.session.get('codigo'):        
        del request.session['codigo']
    if request.session.get('permiso'):
        del request.session['permiso']
    if request.session.get('modulos'):
        del request.session['modulos']
    logout(request)
    return redirect(login)