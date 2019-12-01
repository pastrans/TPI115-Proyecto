function editTiempo(idT, hIni, hFin){
    $("#frmTiempo").attr('action', 'editar/' + idT);
    $("#horaI").val(hIni);
    $("#horaF").val(hFin);
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