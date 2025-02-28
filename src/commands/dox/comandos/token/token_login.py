import sys
import time
import os
from colorama import init, Fore
from selenium import webdriver
import requests
from src.utils.fecha import hora_actual
from src.utils.console import SoloLinux, clear, console

init()

GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED
GREEN = Fore.GREEN
WHITE = Fore.WHITE
RESET = Fore.RESET




def LeerTokensDesdeArchivo():
    try:
        with open("others/tokens.txt", "r") as archivo:
            tokens = [linea.strip() for linea in archivo if linea.strip()]
        return tokens
    except FileNotFoundError:
        print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Las carpeta no se ha encontrado en la ruta")
        sys.exit()
    except Exception:
        print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Consultar a pablo (fallo con token)")
        sys.exit()


def ValidarToken(token):
    url = "https://discord.com/api/v9/users/@me"
    headers = {"Authorization": token}
    try:
        respuesta = requests.get(url, headers=headers)
        return respuesta.status_code == 200
    except Exception:
        print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} No se pudo validar el token")
        return False    




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

        while True:
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
            except Exception:
                print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} No se pudo iniciar el Chrome")
                input(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Enter para continuar...")
                sys.exit()

        elif navegador in ['2', '02']:
            if sys.platform.startswith("linux"):
                SoloLinux()
            else:
                try:
                    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Iniciando Edge...")
                    driver = webdriver.Edge()
                    print(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Se ha preparado Edge con éxito")
                except Exception:
                    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} No se pudo iniciar Edge")
                    input(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Enter para continuar...")
                    sys.exit()

        elif navegador in ['3', '03']:
            if sys.platform.startswith("linux"):
                SoloLinux()
            else:
                try:
                    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Iniciando Firefox...")
                    driver = webdriver.Firefox()
                    print(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Se ha preparado Firefox con éxito")
                except Exception:
                    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} No se pudo iniciar Firefox ")
                    input(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Enter para continuar...")
                    sys.exit()
        else:
            print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Selecciona la opcion valida.")
            sys.exit()

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
            input(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Enter para continuar...")

        except Exception as e:
            print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Hubo un problema al iniciar el navegador o conectar el token: {e}")
            input(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Enter para continuar...")

    except Exception as e:
        print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Consultar a pablo (Error inesperado)")
        sys.exit()


if __name__ == "__main__":
    try:
        token_login()
    except Exception:
        print("\n{GRAY}[{RED}#{GRAY}]{WHITE} Consultar a pablo (Error inesperado)")
        input(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Enter para continuar...")
