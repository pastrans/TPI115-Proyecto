function editPermiso(idPnal, nombre, apellido, codigo){
    $("#frmSeccion").attr('action', 'editar/' + idPnal);
    $("#nombreP").val(nombre);
    $("#apellidoP").val(apellido);
    $("#codigoP").val(codigo);
}

//COMPLETADO
function elimPermiso(idPermiso){
    Swal.fire({
        title: '¿Seguro que desea desactivar el permiso?',
        text: "Los datos relacionados con el permiso ya no serán visibles",
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

function habPnal(idPnal){
    Swal.fire({
        title: '¿Seguro de activar la sección?',
        text: "Los datos relacionados con la sección ahora serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, activar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/personal/cambiarEstado/' + idPnal + '/A'
        }
    });
}

//COMPLETADO
function filtrarSeccion(estado){
    $("#estado").val(estado);
    $("#frmFiltroSeccion").submit();
}