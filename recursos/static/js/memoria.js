datos = JSON.parse(datos.replaceAll("'", '"'))

const inicio = new Date();

var errores = 0;

var envio = false;

var botonSelec = -1;

var bloqueados = [];

var encontrados = [];

var cerrables = [];

cargarBotones();

const botones = document.querySelectorAll(".carta");

asignarComportamientoBotones();

function cargarBotones(){
    for (var i = 0; i < datos.length; i++) {
        document.querySelector(".cartas").innerHTML += `<button class="carta">#</button>`;
    }
}

function asignarComportamientoBotones(){
    for (var i = 0; i < botones.length; i++) {
        var boton = botones[i];
        boton.addEventListener("click", (evento) => {
            boton = evento.path[0];
            var posBoton = -1;
            for (var j = 0; j < botones.length; j++) {
                if (boton == botones[j]) {
                    posBoton = j;
                    break;
                }
            }
            if(!envio){
                evento.preventDefault();
            }else{
                document.querySelector(".tiempo").value = Math.abs(inicio - new Date())/1000/60;
                document.querySelector(".errores").value = errores;
            }
            if(encontrados.length+2==botones.length && !encontrados.includes(posBoton) && !bloqueados.includes(posBoton)){
                envio = true;
            }
            if(!bloqueados.includes(posBoton) && !encontrados.includes(posBoton)){
                bloqueados.push(posBoton);
                boton.style.transform = "rotateY(0deg)";
                boton.innerText = datos[posBoton];
                if (botonSelec < 0) {
                    botonSelec = posBoton;
                } else {
                    if (boton.innerText == botones[botonSelec].innerText){
                        encontrados.push(botonSelec);
                        botones[botonSelec].classList.add("par-encontrado");
                        encontrados.push(posBoton);
                        boton.classList.add("par-encontrado");
                    }else{
                        bloquearTodos();
                        cerrables.push(posBoton);
                        cerrables.push(botonSelec);
                        setTimeout(function () {
                            bloqueados = [];
                            cerrarCartas();
                            errores++;
                        }, 2000);
                    }
                    botonSelec = -1;
                }
            }
        });
    }
}

function eliminarBloqueado(posicion){
    var nuevo = []
    for(var i=0;i<bloqueados.length;i++){
        if(posicion!=bloqueados[i]){
            nuevo.push(bloqueados[i])
        }
    }
    bloqueados = nuevos;
}

function bloquearTodos(){
    for(var i=0;i<botones.length;i++){
        if(!bloqueados.includes(i)){
            bloqueados.push(i);
        }
    }
}

function cerrarCartas(){
    for(var i=0;i<cerrables.length;i++){
        const boton = botones[cerrables[i]];
        boton.style.transform = "rotateY(180deg)";
        boton.innerText = "#";
    }
    cerrables = [];
}