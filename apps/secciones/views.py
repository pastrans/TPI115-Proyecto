from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



def inicio(request):
	if request.user.is_superuser  and request.user.is_staff :
		return render(request, 'secciones/administrar.html')
	else :
		return HttpResponse('Acceso denegado')
