
function editEstudiante(idEstudiante, nombre, apellido, codigo, idSeccionGrado){
    $("#frmSeccion").attr('action', 'editar/' + idEstudiante);
    $("#nombreEstudiante").val(nombre);
    $("#apellidoEstudiante").val(apellido);
    $("#codigoEstudiante").val(codigo);
    $("#seccionGrado").val(idSeccionGrado).change();
    $("#chkCambiar").show();
    $("#LchkCambiar").show();
    $("#claveEstudiante").hide();
    $("#lblclaveEstudiante").hide();
}

function elimEstudiante(idEstudiante){
    Swal.fire({
        title: '¿Seguro que desea desactivar la sección?',
        text: "Los datos relacionados con la sección ya no serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, desactivar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/estudiante/cambiarEstado/' + idEstudiante + '/I'
        }
    });
}

function habEstudiante(idEstudiante){
    Swal.fire({
        title: '¿Seguro que desea activar la sección?',
        text: "Los datos relacionados con la sección ahora serán visibles",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, activar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/estudiante/cambiarEstado/' + idEstudiante + '/A'
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
            $("#claveEstudiante").show();
            $("#lblclaveEstudiante").show();
        }
        else if($(this).prop("checked") == false){
            $("#claveEstudiante").hide();
            $("#lblclaveEstudiante").hide();
        }
    });
});