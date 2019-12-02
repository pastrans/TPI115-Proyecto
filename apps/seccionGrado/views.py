from django.shortcuts import render, redirect
from apps.seccionGrado.models import SeccionGrado
from django.contrib.auth.decorators import login_required

# Código para mostrar una secciongrado (se esetandarizo que secciongrado es una representación fisica de los salones )
@login_required
def resumenSeccionGrado(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    seccionGrados = SeccionGrado.objects.all()
    data = {'seccionGrados' : seccionGrados}
    return render(request, 'seccionGrado/administrar.html', data)

@login_required
# Código para agregar una Grado
def agregarSeccionGrado(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        nombre = request.POST['nombre']
        sg = SeccionGrado(nombre = nombre)
        sg.save()
        return redirect('resumenSeccionGrado')
    return redirect('resumenSeccionGrado')
