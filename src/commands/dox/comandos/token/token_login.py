import sys
import time
from colorama import init, Fore
from selenium import webdriver
import requests
import os

init()

GRAY = '\033[90m'
RED = '\033[91m'
GREEN = '\033[92m'
WHITE = '\033[97m'
RESET = '\033[0m'

def Lento(texto):
    for línea in texto.splitlines():
        print(línea)
        time.sleep(0.05)

def LeerTokensDesdeArchivo():
    try:
        with open("files-2/token/token.txt", "r") as archivo:
            tokens = [linea.strip() for linea in archivo if linea.strip()]
        return tokens
    except FileNotFoundError:
        print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Las carpeta no se ha encontrado en la ruta")
        sys.exit()
    except Exception as e:
        print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Consultar a pablo (fallo con token)")
        sys.exit()

def ValidarToken(token):
    url = "https://discord.com/api/v9/users/@me"
    headers = {"Authorization": token}
    try:
        respuesta = requests.get(url, headers=headers)
        if respuesta.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} No se pudo validar el token")
        return False

def hora_actual():
    return time.strftime("%H:%M:%S")

def SoloLinux():
    print(f"\n {GRAY}[{RED}#{GRAY}]{WHITE} Esta opción solo está disponible para Windows.")
    sys.exit()

def Continuar():
    input(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Enter para contunuar...")

def Reiniciar():
    sys.exit()

def OpciónErrónea():
    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Selecciona la opcion valida.")
    Reiniciar()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def Error(e):
    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Consultar a pablo (Error inesperado)")
    sys.exit()

def token_login():
    try:
        tokens = LeerTokensDesdeArchivo()

        print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Tokens encontrados: ")
        print("")
        token_validez = []
        for i, token in enumerate(tokens, start=1):
            valido = ValidarToken(token)
            estado = f"{GREEN}Valido" if valido else f"{RED}Invalido"
            print(f"{GRAY}[{GREEN}#{GRAY}]{WHITE} Token {estado} | {token}")
            token_validez.append((token, valido))

        while True:  # Bucle para seleccionar un token válido
            seleccion = input(f"\n{GREEN}↪{WHITE}  Selecciona el token: ")

            try:
                indice = int(seleccion) - 1
                if indice < 0 or indice >= len(token_validez):
                    raise ValueError
                token_seleccionado, es_valido = token_validez[indice]
                if es_valido:
                 break
                else:
                    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} El token seleccionado es invalido")
            except ValueError:
                print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} El token seleccionado es invalido")

        print(f"""  
{GRAY}[{RED}#{GRAY}]{WHITE} Chrome {GRAY} [{WHITE}Windows / Linux{GRAY}]{WHITE}
{GRAY}[{RED}#{GRAY}]{WHITE} Edge {GRAY}[{WHITE}Windows{GRAY}]{WHITE}
{GRAY}[{RED}#{GRAY}]{WHITE} Firefox {GRAY}[{WHITE}Windows{GRAY}]{WHITE}""")
        navegador = input(f"\n{GREEN}↪  {WHITE} ")

        if navegador in ['1', '01']:
            try:
                print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Iniciando Chrome...")
                driver = webdriver.Chrome()
                print(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Se ha preparado Chrome con éxito")
            except Exception as e:
                print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} No se pudo iniciar el Chrome")
                Continuar()
                Reiniciar()

        elif navegador in ['2', '02']:
            if sys.platform.startswith("linux"):
                SoloLinux()
            else:
                try:
                    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Iniciando Edge...")
                    driver = webdriver.Edge()
                    print(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Se ha preparado Edge con éxito")
                except Exception as e:
                    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} No se pudo iniciar Edge")
                    Continuar()
                    Reiniciar()

        elif navegador in ['3', '03']:
            if sys.platform.startswith("linux"):
                SoloLinux()
            else:
                try:
                    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Iniciando Firefox...")
                    driver = webdriver.Firefox()
                    print(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Se ha preparado Firefox con éxito")
                except Exception as e:
                    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} No se pudo iniciar Firefox ")
                    Continuar()
                    Reiniciar()
        else:
            OpciónErrónea()

        try:
            script = """
                    function login(token) {
                    setInterval(() => {
                    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"` ;
                    }, 50);
                    setTimeout(() => {
                    location.reload();
                    }, 2500);
                    }
                    """
            driver.get("https://discord.com/login")
            print(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Conectando con Token...")
            driver.execute_script(script + f'\nlogin("{token_seleccionado}")')
            time.sleep(4)
            print(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Token se ha conectado con éxito")
            print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Si cierras la herramienta, el navegador también se cerrará.")
            Continuar()

        except Exception as e:
            print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Hubo un problema al iniciar el navegador o conectar el token: {e}")
            Continuar()

    except Exception as e:
        Error(e)


if __name__ == "__main__":
    try:
        token_login()
    except Exception as e:
        print(f"Consultar pablo")
        print("Consultar pablo")
        Continuar()
