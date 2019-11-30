$(document).ready(function(){
    $("#frmSancion").attr('action', 'agregar');
});

function editarSancion(idSancion, descripcion){
    $("#frmSancion").attr('action', 'editar/' + idSancion);
    $("#descripcion").val(descripcion);
}

function eliminarSancion(idSancion){
    Swal.fire({
        title: '¿Seguro de desactivar la sancion?',
        text: "Los datos de la sancion ya no serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, desactivar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/sancion/cambiarEstado/' + idSancion + '/I'
        }
    });
}

function habilitarSancion(idSancion){
    Swal.fire({
        title: '¿Seguro de activar la sancion?',
        text: "Los datos relacionados con la sancion ahora serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, activar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/sancion/cambiarEstado/' + idSancion + '/A'
        }
    });
}

function filtrarSancion(estado){
    $("#estado").val(estado);
    $("#frmFiltroSancion").submit();
}