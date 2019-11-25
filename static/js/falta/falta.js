$(document).ready(function(){
    $("#frmFalta").attr('action', 'agregar');
});

function editarFalta(idFalta, descripcion, tipo){
    $("#frmFalta").attr('action', 'editar/' + idFalta);
    $("#descripcion").val(descripcion);
    $("#tipo").val(tipo);
}

function eliminarFalta(idFalta){
    Swal.fire({
        title: '¿Seguro de desactivar la falta?',
        text: "Los datos relacionados con la sección ya no serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, desactivar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/falta/cambiarEstado/' + idFalta + '/I'
        }
    });
}

function habilitarFalta(idFalta){
    Swal.fire({
        title: '¿Seguro de activar la Falta?',
        text: "Los datos relacionados con la falta ahora serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, activar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/falta/cambiarEstado/' + idFalta + '/A'
        }
    });
}

function filtrarFalta(estado){
    $("#estado").val(estado);
    $("#frmFiltroFaltas").submit();
}