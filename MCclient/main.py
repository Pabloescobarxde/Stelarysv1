import os
import subprocess
import time
from colorama import init, Fore


R = "\033[31m"
W = "\033[37m"
GRAY = "\033[90m" 
G = "\033[32m"
P = "\033[35m"

def crear_y_ejecutar(nickname, version, version_type, mem_max, mem_min):
    # Ruta del archivo index.js
    archivo_js = "MCclient/src/index.js"
    
    # Nuevo contenido del archivo
    nuevo_contenido = f'''
// github del src https://github.com/Pierce01/MinecraftLauncher-core
// comando para instalar la libreria npm install minecraft-launcher-core
// descargar los modulos de la libreria npm install npm i minecraft-launcher-core
// documentado por pablo / equipo de stelarys

const {{ Client, Authenticator }} = require('minecraft-launcher-core'); // libreria de minecraft-launcher-core
const launcher = new Client(); // creacion de un nuevo cliente

let opts = {{
    authorization: Authenticator.getAuth("{nickname}"), //nickname
    root: "./minecraft", //creacion del directorio src para funcion del mcs
    version: {{
        number: "{version}",   // version del juego
        type: "{version_type}" // tipo de version
    }},
    memory: {{       // tamaño de memoria
        max: "{mem_max}", // maximo de memoria
        min: "{mem_min}"  // minimo de memoria
    }}
}}

launcher.launch(opts); // lanzamiento del juego

launcher.on('debug', (e) => console.log(e));
launcher.on('data', (e) => console.log(e));
'''

    
    os.makedirs(os.path.dirname(archivo_js), exist_ok=True)
    with open(archivo_js, "w", encoding="utf-8") as file:
        file.write(nuevo_contenido)
    
    print(f"\n{GRAY}[{G}#{GRAY}] {GRAY}Iniciando lanzador improvisado{W}")
    time.sleep(2)
    try:
        subprocess.run(["node", archivo_js], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{R}Error al ejecutar index.js: {e}{W}")
    except FileNotFoundError:
        print(f"{R}Error: Node.js no está instalado o no está en el PATH.{W}")

def mcclient():
    init(autoreset=True)
    
    print("")
    nickname = input(f"{GRAY}[{R}#{GRAY}] {W}Nickname: ")
    version = input(f"{GRAY}[{R}#{GRAY}] {W}Version del juego: ")
    version_type = input(f"{GRAY}[{R}#{GRAY}] {W}Ingrese el tipo de versión (release/snapshot): ")
    mem_max = input(f"{GRAY}[{R}#{GRAY}] {W}Maximo de memoria (6G): ")
    mem_min = input(f"{GRAY}[{R}#{GRAY}] {W}Minimo de memoria (4G): ")

    crear_y_ejecutar(nickname, version, version_type, mem_max, mem_min)

if __name__ == "__main__":
    mcclient()
