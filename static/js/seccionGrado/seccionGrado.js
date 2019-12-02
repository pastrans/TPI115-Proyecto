$(document).ready(function(){
    $("#frmSeccionGrado").attr('action', 'agregar');
});
/*
frmSeccionGrado es el id de mi formulario por eso lo trabajo con punto para acceder a las propiedades
para setiar los valores de los input en los html ultilizo # para acceder a sus atributos/propiedades
y luego de eso . val para cambiar la propiedad de value con la variable que me pasan
*/
function editarSeccionGrado(idSeccionGrado, grado, seccion,especialidad, personal, turno ){

    $("#frmSeccionGrado").attr('action', 'editar/' + idSeccionGrado);
    $("#grado").val(grado);
    $("#seccion").val(seccion);
    $("#especialidad").val(especialidad);
    $("#personal").val(personal);
    $("#turno").val(turno);

}
