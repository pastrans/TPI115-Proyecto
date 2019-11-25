$(document).ready(function(){
    $("#frmTipoFalta").attr('action', 'agregar');
});

function editarTipoFalta(idTipo, nombre){
    $("#frmTipoFalta").attr('action', 'editar/' + idTipo);
    $("#nombre").val(nombre);
}

function eliminarTipoFalta(idTipo){
    Swal.fire({
        title: '¿Seguro de desactivar el Tipo De Falta?',
        text: "Los datos relacionados al Tipo Falta ya no serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, desactivar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/tipoFalta/cambiarEstado/' + idTipo + '/I'
        }
    });
}

function habilitarTipoFalta(idTipo){
    Swal.fire({
        title: '¿Seguro de activar el Tipo De Falta?',
        text: "Los datos relacionados con el Tipo Falta ahora serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, activar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/tipoFalta/cambiarEstado/' + idTipo + '/A'
        }
    });
}

function filtrarTipoFalta(estado){
    $("#estado").val(estado);
    $("#frmFiltroTipoFalta").submit();
}