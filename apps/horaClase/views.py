from django.shortcuts import render, redirect
from apps.personal.models import Personal
from apps.horaClase.models import HoraClase
from apps.tiempo.models import Tiempo
import itertools

# Create your views here.
def redirectVacio(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')    
    return render(request, 'index/index.html',None)

def resHorarioPnal(request,idPnal):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    horT = getHorTemplate(idPnal,'P')
    per = Personal.objects.get(idPersonal = idPnal)
    tiempos = getTiempos()
    data = {'horarios' : horT, 'tiempos' : tiempos, 'personal' : per}                
    return render(request, 'horario/horario.html',data)

def resHorarioSecc(request,idSecc):
    if not request.session['tipo'] == 'P':
        return redirect('/my')    
    return render(request, 'horario/horario.html',None)

def getHorarioOrd(id, tipo):
    if tipo == 'P': #viene de personal
        horario = [*HoraClase.objects.filter(personal = id, dia = 'L').order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(personal = id, dia = 'M').order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(personal = id, dia = 'X').order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(personal = id, dia = 'J').order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(personal = id, dia = 'V').order_by('tiempo__horaInicial')]
    elif tipo == 'S': #viene de seccion
        horario = [*HoraClase.objects.filter(seccionGrado = id, dia = 'L').order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(seccionGrado = id, dia = 'M').order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(seccionGrado = id, dia = 'X').order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(seccionGrado = id, dia = 'J').order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(seccionGrado = id, dia = 'V').order_by('tiempo__horaInicial')]
    return horario

def getTiempos():
    tiempo = Tiempo.objects.all()
    return tiempo

def getHorTemplate(id,tipo):
    hor = getHorarioOrd(id,tipo)
    tiempo = getTiempos()    
    HorTem = []    
    ListHora = []
    for t in tiempo:
        cL = 0
        cM = 0
        cX = 0
        cJ = 0
        cV = 0
        ListHora = []
        for h in hor:
            #Dia lunes
            if h.dia == 'L' and h.tiempo.idTiempo == t.idTiempo:
                ListHora.append(h)
                cL = 1            
            #Dia martes
            if h.dia == 'M' and h.tiempo.idTiempo == t.idTiempo:
                if cL == 0: #si estamos en martes y no se agrego nada antes
                    cL = 1
                    ListHora.append(None)
                ListHora.append(h)
                cM = 1
            #Dia Miercoles
            if h.dia == 'X' and h.tiempo.idTiempo == t.idTiempo:
                if cL == 0 or cM == 0: #estando en miercoles y no se agg nada antes
                    #
                    if cL == 0:
                        ListHora.append(None)
                    if cM == 0:
                        ListHora.append(None)                    
                    #
                    cL = 1
                    cM = 1
                ListHora.append(h)
                cX = 1
            #Dia Jueves
            if h.dia == 'J' and h.tiempo.idTiempo == t.idTiempo:
                if cL == 0 or cM == 0 or cX == 0: #estando en jueves y no se agg nada antes
                    #
                    if cL == 0:
                        ListHora.append(None)
                    if cM == 0:
                        ListHora.append(None)
                    if cX == 0:
                        ListHora.append(None)
                    #
                    cL = 1
                    cM = 1
                    cX = 1
                ListHora.append(h)
                cJ = 1
            #Dia Viernes
            if h.dia == 'V' and h.tiempo.idTiempo == t.idTiempo:
                if cL == 0 or cM == 0 or cX == 0 or cJ == 0:
                    #
                    if cL == 0:
                        ListHora.append(None)
                    if cM == 0:
                        ListHora.append(None)
                    if cX == 0:
                        ListHora.append(None)
                    if cJ == 0:
                        ListHora.append(None)
                    #
                    cL = 1
                    cM = 1
                    cX = 1
                    cJ = 1
                ListHora.append(h)
                cV = 1
        #verificando los no apendiados
        if cL == 0:
            ListHora.append(None)
        if cM == 0:
            ListHora.append(None)
        if cX == 0:
            ListHora.append(None)
        if cJ == 0:
            ListHora.append(None)
        if cV == 0:
            ListHora.append(None)
        HorTem.append(ListHora)
    return HorTem

def contNoneLst(cl,cm,cx,cj,cv):
    cont = 0
    if cl == 0:
        cont += 1
    if cm == 0:
        cont += 1
    if cx == 0:
        cont += 1
    if cj == 0:
        cont +=1
    if cv == 0:
        cont +=1
    return cont