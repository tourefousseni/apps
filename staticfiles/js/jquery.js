alert("La page a été actualisée avec success !");

$(document).ready(function(){
$("#status").on('click', function () {
  var getValue= $("#personne").val();
   alert(getValue);
 });
});
