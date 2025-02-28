import os
import time
import sys
from colorama import init, Fore, Style
from src.commands.entrada import Letra, skibidi



init(autoreset=True)


RED = "\033[31m"
GREEN = "\033[32m"
LIGHT_BLUE = "\033[94m"
WHITE = "\033[37m"
PURPLE = "\033[35m"




dibujo1 = f"""



{RED} ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄      ▄▀▀█▄   ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▀▀▄  ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄     
{RED}█ █   ▐ █    █  ▐ ▐  ▄▀   ▐ █    █      ▐ ▄▀ ▀▄ █   █   █ █   ▀▄ ▄▀ █ █   ▐ █    █  ▐ █      █ █      █ █    █      
{RED}   ▀▄   ▐   █       █▄▄▄▄▄  ▐    █        █▄▄▄█ ▐  █▀▀█▀  ▐     █      ▀▄   ▐   █     █      █ █      █ ▐    █      
{WHITE}▀▄   █     █        █    ▌      █        ▄▀   █  ▄▀    █        █   ▀▄   █     █      ▀▄    ▄▀ ▀▄    ▄▀     █       
{WHITE}█▀▀▀    ▄▀        ▄▀▄▄▄▄     ▄▀▄▄▄▄▄▄▀ █   ▄▀  █     █       ▄▀     █▀▀▀    ▄▀         ▀▀▀▀     ▀▀▀▀     ▄▀▄▄▄▄▄▄▀ 
{WHITE} ▐      █          █    ▐     █         ▐   ▐   ▐     ▐       █      ▐      █                             █         
{WHITE}        ▐          ▐          ▐                               ▐             ▐                             ▐         


       Bienvenido a {RED}Stelarys{WHITE}Tool | 1.0v

"""

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def centrar_texto(dibujo):
    ancho_consola = os.get_terminal_size().columns
    lineas = dibujo.splitlines()
    dibujo_centrado = ""
    for linea in lineas:
        espacios = (ancho_consola - len(linea)) // 2
        dibujo_centrado += " " * espacios + linea + "\n"
    return dibujo_centrado

def imprimir_rojo_5s(dibujo):
    print(f"{dibujo}{Style.RESET_ALL}")
    time.sleep(1)

clear_console()

dibujo1_centrado = centrar_texto(dibujo1)
imprimir_rojo_5s(dibujo1_centrado)

clear_console()

Letra()
skibidi()
