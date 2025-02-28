import webbrowser
import requests
import time
from datetime import datetime

BEFORE = "\033[1;34m"
AFTER = "\033[0m"
INFO_ADD = "\033[1;32m"
WHITE = "\033[1;37m"
RED = "\033[1;31m"
WAIT = "\033[1;33m"
RESET = "\033[0m"
GRAY = "\033[1;30m"
GREEN = "\033[1;32m"

def hora_actual():
    return datetime.now().strftime("%H:%M:%S")

def ErrorModulo(e):
    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} error en el modulo")

def ErrorId():
    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} La id del bot es invalida")

def Error(e):
    print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} error invalido")

def Titulo(titulo):
    print(f"\n{'-'*50}\n{titulo}\n{'-'*50}\n")

def Lento(texto):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

def invite_bot_id():
    try:
        try:
            IdBot = int(input(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Proporcione la id del bot: "))
        except ValueError:
            ErrorId()

        url_invitacion = f'https://discord.com/oauth2/authorize?client_id={IdBot}&scope=bot&permissions=8'
        try:
            respuesta = requests.get(url_invitacion)
            print(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} URL de invitación: {GRAY}[{WHITE}{url_invitacion}{GRAY}]")
        except requests.RequestException as e:
            ErrorModulo(e)

        eleccion = input(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Deseas abrir el navegador (s/n) ")
        if eleccion.lower() in ['s', 'si']:
            webbrowser.open_new_tab(url_invitacion)

    except Exception as e:
        Error(e)

if __name__ == "__main__":
  pass