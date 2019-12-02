$(document).ready(function(){
    //$("#falta_id").hide();
    //$("#faltaLabel").hide();
    $("#tipoFalta").change(function(){
        $("#falta_id").val(0);
        $("#faltaLabel").show();
        $("#falta_id").show();
        $("#falta_id").children().hide();
        $(".tipoFalta" + $("#tipoFalta").val()).show();
        $("#falta_id option[value=0]").show();
    });
});

function eliminar(idAmonestacion){
    Swal.fire({
        title: '¿Seguro de eliminar la amonestación?',
        text: "No se podrá recuperar la amonestación",
        type: 'info',
        showCancelButton: true,
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar'
        }).then((result) => {
        if (result.value) {
            location.href = '/amonestacion/eliminar/' + idAmonestacion
        }
    });
}

function verReporte(){
    $("#idEstudiante").val($("#estudiante").val());
    $("#frmReporte").submit();
}