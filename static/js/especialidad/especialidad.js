function editarEspecialidad(idEspecialidad, nombre){
    $("#frmSeccion").attr('action', 'editar/' + idEspecialidad);
    $("#nombre").val(nombre);
}

function eliminarEspecialidad(idEspecialidad){
    Swal.fire({
        title: '¿Seguro de desactivar la especialidad?',
        text: "Los datos relacionados con la especialidad ya no serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, desactivar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/especialidad/cambiarEstado/' + idEspecialidad + '/B'
        }
    });
}

function habilitarEspecialidad(idEspecialidad){
    Swal.fire({
        title: '¿Seguro de activar la especialidad?',
        text: "Los datos relacionados con la especialidad ahora serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, activar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/especialidad/cambiarEstado/' + idEspecialidad + '/A'
        }
    });
}

function filtrarEspecialidad(estado){
    $("#estado").val(estado);
    $("#frmFiltroSeccion").submit();
}