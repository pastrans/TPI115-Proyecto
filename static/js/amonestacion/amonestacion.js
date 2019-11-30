$(document).ready(function(){
    $("#falta_id").hide();
    $("#faltaLabel").hide();
    $("#tipoFalta").change(function(){
        $("#falta_id").show();
        $("#falta_id").children().hide();
        $(".tipoFalta" + $("#tipoFalta").val()).show();
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