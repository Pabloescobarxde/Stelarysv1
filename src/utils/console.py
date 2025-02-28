import os, shutil, sys
from colorama import init, Fore

init(autoreset=True)

GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED
GREEN = Fore.GREEN
WHITE = Fore.WHITE
RESET = Fore.RESET

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def center(arg):
    ancho_consola = os.get_terminal_size().columns
    lineas = arg.splitlines()
    dibujo_centrado = ""
    for linea in lineas:
        espacios = (ancho_consola - len(linea)) // 2
        dibujo_centrado += " " * espacios + linea + "\n"
    return dibujo_centrado

def centrar_texto(texto):
    terminal_ancho = shutil.get_terminal_size().columns
    for linea in texto.split("\n"):
        print(" " * ((terminal_ancho - len(linea)) // 2) + linea)
        
def SoloLinux():
    print(f"\n {GRAY}[{RED}#{GRAY}]{WHITE} Esta opción solo está disponible para Windows.")
    sys.exit()