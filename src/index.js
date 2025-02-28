
// github del src https://github.com/Pierce01/MinecraftLauncher-core
// comando para instalar la libreria npm install minecraft-launcher-core
// descargar los modulos de la libreria npm install npm i minecraft-launcher-core
// documentado por pablo / equipo de stelarys

const { Client, Authenticator } = require('minecraft-launcher-core'); // libreria de minecraft-launcher-core
const launcher = new Client(); // creacion de un nuevo cliente

let opts = {
    authorization: Authenticator.getAuth("Roctups"), //nickname
    root: "./minecraft", //creacion del directorio src para funcion del mcs
    version: {
        number: "1.20",   // version del juego
        type: "release" // tipo de version
    },
    memory: {       // tamaño de memoria
        max: "6G", // maximo de memoria
        min: "4G"  // minimo de memoria
    }
}

launcher.launch(opts); // lanzamiento del juego

launcher.on('debug', (e) => console.log(e));
launcher.on('data', (e) => console.log(e));
