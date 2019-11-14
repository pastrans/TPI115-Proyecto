$(document).ready(function(){
    $("#frmSeccion").attr('action', 'agregar');
});
function editarSeccion(idSeccion, nombre){
    $("#frmSeccion").attr('action', 'editar/' + idSeccion);
    $("#nombre").val(nombre);
}

function eliminarSeccion(idSeccion){
    Swal.fire({
        title: '¿Seguro de desactivar la sección?',
        text: "Los datos relacionados con la sección ya no serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, desactivar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/seccion/eliminar/' + idSeccion
        }
    });
}

function filtrarSeccion(estado){
    $("#estado").val(estado);
    $("#frmFiltroSeccion").submit();
}