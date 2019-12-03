$("#hoy").change(function(){
    if ($("#hoy").is(":checked")){
        $("#fecha").prop('disabled', true);
    }else{
        $("#fecha").prop('disabled', false);
    }
});
$("#horaServer").change(function(){
    if ($("#horaServer").is(":checked")){
        $("#hora").prop('disabled', true);
    }else{
        $("#hora").prop('disabled', false);
    }
});