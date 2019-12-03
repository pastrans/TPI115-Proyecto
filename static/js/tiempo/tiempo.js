function editTiempo(idT, hIni, hFin){
    $("#frmTiempo").attr('action', 'editar/' + idT);

    $("#horaI").val(handleTiempo(hIni));
    $("#horaF").val(handleTiempo(hFin));
}

function handleTiempo(h){
    t24 = "";
    separador = " ";
    limite = 2;
    arrHora = h.split(separador,limite);
    //verificando si es pm o am
    suma = 0;
    if (arrHora[1].substring(0,1) == 'p'){
        suma = 12;
    }
    //tratando la hora
    hora = ""
    if (arrHora[0].includes(":")){
        horaDiv = arrHora[0].split(":");        
        hora = parseInt(horaDiv[0]) + parseInt(suma);
        mins = horaDiv[1];
    }else{        
        hora = parseInt(arrHora[0]) + parseInt(suma);
        mins = "00";
    }
    hora = "" + hora;    
    if (hora.length == 1){
        var newHd = "0" + hora;
        hora = newHd;
    }
    t24 = hora + ":" + mins; 
    return t24
}

function elimTiempo(idPnal){
    Swal.fire({
        title: '¿Seguro de desactivar la sección?',
        text: "Los datos relacionados con la sección ya no serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, desactivar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/tiempo/cambiarEstado/' + idPnal + '/I'
        }
    });
}

function habTiempo(idPnal){
    Swal.fire({
        title: '¿Seguro de activar la sección?',
        text: "Los datos relacionados con la sección ahora serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, activar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/tiempo/cambiarEstado/' + idPnal + '/A'
        }
    });
}

function filtrarEstado(estado){
    $("#estado").val(estado);
    $("#frmFiltro").submit();
}