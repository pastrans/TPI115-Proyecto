from django.shortcuts import render, redirect
from apps.seccionGrado.models import SeccionGrado
from apps.grado.models import Grado
from apps.seccion.models import Seccion
from apps.personal.models import Personal
from apps.especialidad.models import Especialidad
from django.contrib.auth.decorators import login_required
import datetime

# Código para mostrar una secciongrado (se esetandarizo que secciongrado es una representación fisica de los salones )
@login_required
def resumenSeccionGrado(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    x = datetime.datetime.now()
    anio = x.year
    seccionGrados = SeccionGrado.objects.filter(anio= anio)
    grados = Grado.objects.filter(estado="A")
    secciones = Seccion.objects.filter(estado="A")
    personals = Personal.objects.filter(estado="A")
    especialidades = Especialidad.objects.filter(estado="A")
    data = {'seccionGrados' : seccionGrados, 'grados':grados , 'secciones':secciones,'personals':personals, 'especialidades':especialidades}
    return render(request, 'seccionGrado/administrar.html', data)

@login_required
# Código para agregar una SeccionGrado
def agregarSeccionGrado(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        x = datetime.datetime.now()
        anio = x.year
        grado = request.POST['grado']
        seccion = request.POST['seccion']
        especialidad = request.POST['especialidad']
        personal = request.POST['personal']
        turno = request.POST['turno']
        sg = SeccionGrado(grado_id = grado, anio=anio , seccion_id=seccion, especialidad_id=especialidad, personal_id=personal , turno =turno)
        sg.save()
        return redirect('resumenSeccionGrado')
    return redirect('resumenSeccionGrado')

# Código para editar una SeccionGrado
@login_required
def editarSeccionGrado(request, idSeccionGrado):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        sg = SeccionGrado.objects.get(idSeccionGrado = idSeccionGrado)
        sg.grado_id = request.POST['grado']
        sg.seccion_id = request.POST['seccion']
        sg.especialidad_id=request.POST['especialidad']
        sg.personal_id=request.POST['personal']
        sg.turno = request.POST['turno']
        sg.save()
        return redirect('resumenSeccion')
    return redirect('resumenSeccion')
