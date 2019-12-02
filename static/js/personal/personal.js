
function editPnal(idPnal, nombre, apellido, codigo, idPermiso){
    $("#frmSeccion").attr('action', 'editar/' + idPnal);
    $("#nombreP").val(nombre);
    $("#apellidoP").val(apellido);
    $("#codigoP").val(codigo);
    $("#permisoP").val(idPermiso).change();
    $("#chkCambiar").show();
    $("#LchkCambiar").show();
    $("#claveP").hide();
    $("#LclaveP").hide();
}

function elimPnal(idPnal){
    Swal.fire({
        title: '¿Seguro de desactivar la sección?',
        text: "Los datos relacionados con la sección ya no serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, desactivar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/personal/cambiarEstado/' + idPnal + '/I'
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

function filtrarSeccion(estado){
    $("#estado").val(estado);
    $("#frmFiltroSeccion").submit();
}


$(document).ready(function(){
    $("#chkCambiar").hide();
    $("#LchkCambiar").hide();
    $('#chkCambiar').click(function(){
        if($(this).prop("checked") == true){
            $("#claveP").show();
            $("#LclaveP").show();
        }
        else if($(this).prop("checked") == false){
            $("#claveP").hide();
            $("#LclaveP").hide();
        }
    });
});