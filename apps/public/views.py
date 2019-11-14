from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    if not request.session['tipo'] == 'E':
        return redirect('index')
    return render(request, 'public/index.html')