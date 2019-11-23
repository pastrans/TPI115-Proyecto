from django.shortcuts import render
import csv, io
from apps.estudiante.models import Estudiante
from apps.inasistencia.models import Inasistencia

# Create your views here.
def pasarAsistencia(request):
    estudiantes = Estudiante.objects.all()[:10]
    inasistencias = set()
    if request.method == 'POST':
        estudiantesIDs = list(map(int, request.POST.getlist('asistencias')))
        for estudiante in estudiantes:
            if not estudiante.idEstudiante in estudiantesIDs:
                i = Inasistencia(estudiante=estudiante)
                i.save()
                inasistencias.add(estudiante.codigo)
    data = {'estudiantes' : estudiantes, 'inasistencias' : inasistencias}
    return render(request, 'asistencia/administrar.html', data)

def importCsv(request, fecha):
    f = fecha
    estudiantes = set()
    if request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return render(request, 'asistencia/csv.html', {"error" : "NO ES POSIBLE ABRIR EL ARCHIVO"})
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            alumno = Estudiante(
                nombre = column[0],
                apellido = column[1],
                codigo = column[2]
            )
            alumno.save()
            estudiantes.add(column[2])
    context = {'estudiantes' : estudiantes, 'fecha' : f}
    return render(request, 'asistencia/csv.html', context)