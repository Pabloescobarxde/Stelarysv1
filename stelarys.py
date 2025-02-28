import os
import time
from colorama import init, Fore, Style
from src.commands.entrada import Letra, skibidi
from src.utils.console import clear, center
init(autoreset=True)


dibujo1 = f"""
{Fore.RED} ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄      ▄▀▀█▄   ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▀▀▄  ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄     
{Fore.RED}█ █   ▐ █    █  ▐ ▐  ▄▀   ▐ █    █      ▐ ▄▀ ▀▄ █   █   █ █   ▀▄ ▄▀ █ █   ▐ █    █  ▐ █      █ █      █ █    █      
{Fore.RED}   ▀▄   ▐   █       █▄▄▄▄▄  ▐    █        █▄▄▄█ ▐  █▀▀█▀  ▐     █      ▀▄   ▐   █     █      █ █      █ ▐    █      
{Fore.WHITE}▀▄   █     █        █    ▌      █        ▄▀   █  ▄▀    █        █   ▀▄   █     █      ▀▄    ▄▀ ▀▄    ▄▀     █       
{Fore.WHITE}█▀▀▀    ▄▀        ▄▀▄▄▄▄     ▄▀▄▄▄▄▄▄▀ █   ▄▀  █     █       ▄▀     █▀▀▀    ▄▀         ▀▀▀▀     ▀▀▀▀     ▄▀▄▄▄▄▄▄▀ 
{Fore.WHITE} ▐      █          █    ▐     █         ▐   ▐   ▐     ▐       █      ▐      █                             █         
{Fore.WHITE}        ▐          ▐          ▐                               ▐             ▐                             ▐         

       Bienvenido a {Fore.RED}Stelarys{Fore.WHITE}Tool | 1.0v
"""
dibujo1_centrado = center(dibujo1)


def dibujo(dibujo):
    print(f"{dibujo}{Style.RESET_ALL}")
    time.sleep(1)


def main():
    clear()
    dibujo(center(dibujo1))
    clear()
    Letra()
    skibidi()

if __name__ == "__main__":
    main()