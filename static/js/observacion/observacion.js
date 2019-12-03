function editPermiso(idPermiso){
    location.href = '/permiso/editarPermiso/' + idPermiso
}

function elimPermiso(idPermiso){
    Swal.fire({
        title: '¿Seguro que desea desactivar el permiso?',
        text: "Los datos relacionados con el permiso ya no serán visibles.",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, desactivar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/permiso/cambiarEstado/' + idPermiso + '/I'
        }
    });
}

function habPermiso(idPermiso){
    Swal.fire({
        title: '¿Seguro que desea activar el permiso?',
        text: "Los datos relacionados con el permiso ahora serán visibles.",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, activar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/permiso/cambiarEstado/' + idPermiso + '/A'
        }
    });
}

function filtrarSeccion(estado){
    $("#estado").val(estado);
    $("#frmFiltroSeccion").submit();
}