from django.shortcuts import render, redirect
from apps.personal.models import Personal
from apps.horaClase.models import HoraClase
from apps.tiempo.models import Tiempo
from apps.seccionGrado.models import SeccionGrado
from apps.asignatura.models import Asignatura
from datetime import datetime
from django.contrib.auth.decorators import login_required
import itertools

# Create your views here.
@login_required
def redirectVacio(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')    
    return render(request, 'index/index.html',None)

@login_required
def resHorarioPnal(request,idPnal):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    horasT = getHorTemplate(idPnal,'P')    
    per = Personal.objects.get(idPersonal = idPnal)
    tiempos = getTiempos()
    lstPersonal = Personal.objects.filter(estado = 'A')
    today = datetime.today()
    lstSecciones = SeccionGrado.objects.filter(anio = today.year)    
    listAsig = Asignatura.objects.filter(estado = 'A')
    horT = zip(horasT,tiempos)
    data = {'horarios' : horT, 'tiempos' : tiempos, 'personal' : per, 'seccionGrado' : None, 'lstSecc' : lstSecciones, 'lstPer' : lstPersonal, 'lstAsig' : listAsig} #Per p/ identificar
    return render(request, 'horario/horario.html',data)

@login_required
def resHorarioSecc(request,idSecc):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    horasT = getHorTemplate(idSecc,'S')
    secc = SeccionGrado.objects.get(idSeccionGrado = idSecc)
    tiempos = getTiempos()
    lstPersonal = Personal.objects.filter(estado = 'A')
    today = datetime.today()
    lstSecciones = SeccionGrado.objects.filter(anio = today.year)    
    listAsig = Asignatura.objects.filter(estado = 'A')
    horT = zip(horasT,tiempos)
    data = {'horarios' : horT, 'tiempos' : tiempos, 'seccionGrado' : secc, 'personal' : None, 'lstSecc' : lstSecciones, 'lstPer' : lstPersonal, 'lstAsig' : listAsig} #secc p/ identificar
    return render(request, 'horario/horario.html',data)

@login_required
def agregarHoraClase(request):
    if not request.session['tipo'] == 'P':
        return redirect('/my')
    if request.method == 'POST':
        origen = request.POST['idOrigenHorario']
        asignatura = Asignatura.objects.get(idAsignatura = request.POST['asignaturaH'])
        personal = Personal.objects.get(idPersonal = request.POST['personalH'])
        seccGrado = SeccionGrado.objects.get(idSeccionGrado = request.POST['seccionH'])
        dia = request.POST['diaH']
        tiempo = Tiempo.objects.get(idTiempo = request.POST['tiempoH'])
        #validando que el horario agregado no tenga el personal o la seccion en la hora deseada
        if ValidarChoque(tiempo,dia,personal,seccGrado):
            horaC = HoraClase(asignatura = asignatura, seccionGrado = seccGrado, personal = personal, tiempo = tiempo, dia = dia)
            horaC.save()
        else:
            error = "Ya esta ocupado :'v"
        urlRED = ''
        if origen == 'Per':
            urlRED = '/horaClase/horarioPersonal/' + str(personal.idPersonal)
        else:
            urlRED = '/horaClase/horarioSeccion/' + str(seccGrado.idSeccionGrado)
    return redirect (urlRED)

@login_required
def eliminarHoraClase(request,strOrigen,idHC):
    arrO = strOrigen.split('-')
    hClase = HoraClase.objects.get(idHoraClase = idHC)
    hClase.delete()
    red = ''
    if arrO[0] == 'P':
        red = '/horaClase/horarioPersonal/' + str(arrO[1])
    else:
        red = '/horaClase/horarioSeccion/' + str(arrO[1])
    return redirect (red)

def ValidarChoque(tiempo, dia, personal, seccionG):
    today = datetime.today()
    # horario via personal 
    Hor1 = HoraClase.objects.filter(personal = personal.idPersonal, dia = dia, tiempo = tiempo.idTiempo, seccionGrado__anio = today.year)
    #horario via seccionGrado
    Hor2 = HoraClase.objects.filter(seccionGrado = seccionG.idSeccionGrado, dia = dia, tiempo = tiempo.idTiempo, seccionGrado__anio = today.year)
    #Validando (tienen que ser null para agg)
    val = False
    if not Hor1.exists() and not Hor2.exists(): #hay espacio para agregar
        val = True
    return val

def getHorarioOrd(id, tipo):
    today = datetime.today()
    if tipo == 'P': #viene de personal
        horario = [*HoraClase.objects.filter(personal = id, dia = 'L', seccionGrado__anio = today.year).order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(personal = id, dia = 'M', seccionGrado__anio = today.year).order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(personal = id, dia = 'X', seccionGrado__anio = today.year).order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(personal = id, dia = 'J', seccionGrado__anio = today.year).order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(personal = id, dia = 'V', seccionGrado__anio = today.year).order_by('tiempo__horaInicial')]
    elif tipo == 'S': #viene de seccion
        horario = [*HoraClase.objects.filter(seccionGrado = id, dia = 'L', seccionGrado__anio = today.year).order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(seccionGrado = id, dia = 'M', seccionGrado__anio = today.year).order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(seccionGrado = id, dia = 'X', seccionGrado__anio = today.year).order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(seccionGrado = id, dia = 'J', seccionGrado__anio = today.year).order_by('tiempo__horaInicial'),
        *HoraClase.objects.filter(seccionGrado = id, dia = 'V', seccionGrado__anio = today.year).order_by('tiempo__horaInicial')]
    return horario

def getTiempos():
    tiempo = Tiempo.objects.all().order_by('horaInicial')
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