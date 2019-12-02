$(document).ready(function(){
    $("#frmGrado").attr('action', 'agregar');
});

function editarGrado(idGrado, nombre, nivel){
    $("#frmGrado").attr('action', 'editar/' + idGrado);
    $("#nombre").val(nombre);
    $("#nivel").val(nivel);
    console.log(nivel);
}

function eliminarGrado(idGrado){
    Swal.fire({
        title: '¿Seguro de desactivar el grado?',
        text: "Los datos relacionados con grado ya no serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, desactivar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/grado/cambiarEstado/' + idGrado + '/I'
        }
    });
}

function habilitarGrado(idGrado){
    Swal.fire({
        title: '¿Seguro de activar el grado?',
        text: "Los datos relacionados con grado ahora serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, activar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/grado/cambiarEstado/' + idGrado + '/A'
        }
    });
}

function filtrarGrado(estado){
    $("#estado").val(estado);
    $("#frmFiltroGrado").submit();
}
