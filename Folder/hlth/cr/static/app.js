let errorlogin = document.querySelector('ul.errorlist');

if( errorlogin != null ){

errorlogin.removeChild(errorlogin.lastElementChild);
let parrafo  = document.createElement("p");
parrafo.classList.add("alert", "alert-danger", "w-50");
let textoError = document.createTextNode("error al ingresar usuario o contraseña");
parrafo.appendChild(textoError);
errorlogin.appendChild(parrafo);
}


let oklogin =  document.querySelector('#autenticado-ok');

if ( oklogin != null ){
    let elementoParrafo = document.createElement("p");
    elementoParrafo.classList.add("alert", "alert-success");
    let textoIngreso = document.createTextNode("¡Excelente, has Iniciado Sesión!");
    elementoParrafo.appendChild(textoIngreso);
    miNodo = document.querySelector('.container.content-autenticado');
    
setTimeout(() => { miNodo.appendChild(elementoParrafo); }, 500);

}
// let oklogin =  document.querySelector('.container.content-autenticado');
// if ( oklogin != null ){
// Swal.fire({
//     position: 'top-end',
//     icon: 'success',
//     title: 'Your work has been saved',
//     showConfirmButton: false,
//     timer: 1500
//   })
// }


function openNav() {
  document.getElementById("mySidepanel").style.width = "200px";
}

function closeNav() {
  document.getElementById("mySidepanel").style.width = "0";
}




function openForm() {
document.getElementById("chatbotpanel").style.display = "flex";
document.getElementById("chatbotpanel").style.position = "fixed";
//document.getElementById("chatbotpanel").style.position = "fixed";
}

function closeForm() {
document.getElementById("chatbotpanel").style.display = "none";
}
