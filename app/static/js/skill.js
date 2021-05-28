function updateTextInput(val) {
    document.getElementById('textInput').value=val; 
  }
  /*Other field*/
  function changeradioother(){
	  var other= document.getElementById("other");
	  other.value=document.getElementById("inputother").value;
	  }
function setRequired(){

	document.getElementById("inputother").required=true;
}

function removeRequired(){
if(document.getElementById("inputother").required == true){
	document.getElementById("inputother").required=false;
}
}
$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();   
  });

