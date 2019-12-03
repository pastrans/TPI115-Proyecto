function eliminarObservacion(idObservacion){
    Swal.fire({
        title: '¿Seguro que desea eliminar la observación?',
        text: "Los datos relacionados con la observación serán eliminados.",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/observacion/eliminarObservacion/' + idObservacion
        }
    });
}