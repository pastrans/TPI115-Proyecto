from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#import io
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from django.views.generic import View
from django.utils import timezone
from apps.estudiante.models import Estudiante
from apps.amonestacion.models import Amonestacion
from apps.impuntualidad.models import Impuntualidad
from apps.inasistencia.models import Inasistencia
from apps.observacion.models import Observacion

# Create your views here.
@login_required
def index(request):
    if not request.session['tipo'] == 'E':
        return redirect('/index')
    return render(request, 'public/index.html')

class Pdf(View):
    def get(self, request):
        """if not request.session['tipo'] == 'E' or request.session['tipo'] == 'P':
            return redirect('index')"""
       
        today = timezone.now()
        estudiante = Estudiante.objects.get(idEstudiante=request.session['id'])
        amonestaciones = Amonestacion.objects.filter(estudiante=estudiante).order_by('fecha')
        llegadasTarde = Impuntualidad.objects.filter(estudiante=estudiante).order_by('fecha')
        inasistencias = Inasistencia.objects.filter(estudiante=estudiante).order_by('fecha')
        observaciones = Observacion.objects.filter(estudiante=estudiante).order_by('fecha')
        params = {
            'observaciones' : observaciones,
            'inasistencias' : inasistencias,
            'llegadasTarde' : llegadasTarde,
            'amonestaciones' : amonestaciones,
            'estudiante' : estudiante,
            'today': today,
            'request': request
        }
        return Render.render('public/pdf.html', params)

class Render:

    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)