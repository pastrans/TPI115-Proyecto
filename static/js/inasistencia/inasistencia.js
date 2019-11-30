$(document).ready(function(){
    $("#fecha").change(function(){
        d = $("#fecha").val().substring(8,10)
        m = $("#fecha").val().substring(5,7)
        a = $("#fecha").val().substring(0,4)
        $("#btnDiferida").attr("href", "diferida/" + $("#seccionGrado").val() + "/" + d + m + a)
    });
    $("#seccionGrado").change(function(){
        d = $("#fecha").val().substring(8,10)
        m = $("#fecha").val().substring(5,7)
        a = $("#fecha").val().substring(0,4)
        $("#btnDiferida").attr("href", "diferida/" + $("#seccionGrado").val() + d + m + a)
    });
});