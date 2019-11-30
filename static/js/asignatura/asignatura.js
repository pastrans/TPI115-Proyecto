$(document).ready(function(){
    $("#frmAsignatura").attr('action', 'agregar');
});

function editarAsignatura(idAsignatura, nombre){
    $("#frmAsignatura").attr('action', 'editar/' + idAsignatura);
    $("#nombre").val(nombre);
}

function eliminarAsignatura(idAsignatura){
    Swal.fire({
        title: '¿Seguro de desactivar la asignatura?',
        text: "Los datos relacionados con la asignatura ya no serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, desactivar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/asignatura/cambiarEstado/' + idAsignatura + '/I'
        }
    });
}

function habilitarAsignatura(idAsignatura){
    Swal.fire({
        title: '¿Seguro de activar la asignatura?',
        text: "Los datos relacionados con la asignatura ahora serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, activar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/asignatura/cambiarEstado/' + idAsignatura + '/A'
        }
    });
}

function filtrarAsignatura(estado){
    $("#estado").val(estado);
    $("#frmFiltroAsignatura").submit();
}