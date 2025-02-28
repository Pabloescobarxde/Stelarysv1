from src.Utils.discord_estado import init_discord, update_presence
from src.commands.skibidi.help import show_help
from src.commands.skibidi.server import get_server_info
from src.commands.skibidi.ipinfo import obtener_info_de_ip
from src.commands.skibidi.jugador import check_premium, get_username_history, display_results
# from src.commands.skibidi.search import Command as SearchCommand
from src.commands.skibidi.shodan import Command as ShodanCommand
from src.commands.skibidi.scan import Command as ScanCommand
from src.commands.skibidi.ddos import Command as DDoSCommand
#from src.commands.skibidi.dehash import Command as HashCommand
from src.commands.skibidi.subdominio import Command as DominioCommand
from src.commands.skibidi.conectar import Command as ConnectCommand
from src.commands.skibidi.Lookserver import Command as LookserverCommand
from src.commands.doxxing import menu_simplify, doxing
#from src.commands.skibidi.scraper import Command as ScraperCommand
from MCclient.main import mcclient
import time
import os   
import shutil
import sys
import datetime
import sys
import shutil
import importlib
from mccolors import mcwrite, mcreplace
from colorama import init, Fore, Style


R = "\033[31m"
W = "\033[37m"
GRAY = "\033[90m" 
G = "\033[32m"
P = "\033[35m"

init()

def Letra():

    letra_arci = f"""
    
  {R}███████╗████████╗███████╗██╗      █████╗ ██████╗ ██╗   ██╗███████╗           
  {R}██╔════╝╚══██╔══╝██╔════╝██║     ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝     
  {R}███████╗   ██║   █████╗  ██║     ███████║██████╔╝ ╚████╔╝ ███████╗                                    
  {W}╚════██║   ██║   ██╔══╝  ██║     ██╔══██║██╔══██╗  ╚██╔╝  ╚════██║              
  {W}███████║   ██║   ███████╗███████╗██║  ██║██║  ██║   ██║   ███████║        
  {W}╚══════╝   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝                                      

  {GRAY}[{W}StelarysTool {GRAY}-{W} Comienza con {G} Help{GRAY} {R}By Pablo{GRAY}]
    """
    print(letra_arci)

    

current_menu = 0

def centrar_texto(texto):
    terminal_ancho = shutil.get_terminal_size().columns
    for linea in texto.split('\n'):
        print(" " * ((terminal_ancho - len(linea)) // 2) + linea)

def clear_console():

    os.system('cls' if os.name == 'nt' else 'clear')


def skibidi():
   ## init_discord() llama al rpc de discord
   ## update_presence()
    global current_menu
    while True:
        opcion = input(Fore.RED +
                   "┌───[Bienvenido@discord.gg/astralix]\n"
                   "└──$ " + Style.RESET_ALL)

        try:
            if opcion == 'help':
                show_help()  


            elif opcion == 'doxing':
                clear_console()
                doxing()
                menu_simplify()

            elif opcion == 'clear':
                clear_console()  
                Letra()

            #elif opcion.startswith('search '):
            #    argumentos = opcion.split(' ')[1:]
              #  comando_search = SearchCommand()
               # comando_search.run(argumentos)
               # time.sleep(3)

            elif opcion.startswith('check '):  
                nickname = opcion.split(' ', 1)[1]
                uuid, status = check_premium(nickname)  
                if uuid:
                    history = get_username_history(uuid)  
                    display_results(nickname, uuid, status, history)
                else:
                    display_results(nickname, uuid, status, None)
                    
            elif opcion.startswith('ipinfo '):  
                ip = opcion.split(' ', 1)[1]  
                url_mapa = obtener_info_de_ip(ip)  
                print(f"URL del Mapa: {url_mapa}")

            elif opcion.startswith('server '):  
                ip = opcion.split(' ', 1)[1]
                get_server_info(ip)

            elif opcion.startswith('shodan '):
               argumentos = opcion.split(' ')[1:] 
               comando_shodan = ShodanCommand()
               comando_shodan.run(argumentos)
               time.sleep(3)
            
            elif opcion.startswith('scan'):
                argumentos = opcion.split(' ')[1:]
                comando_scan = ScanCommand()
                comando_scan.run(argumentos)
                time.sleep(3)
            
            elif opcion.startswith('ddos'):
                argumentos = opcion.split(' ')[1:]
                comando_ddos = DDoSCommand()
                comando_ddos.run(argumentos)
                time.sleep(3)

            #elif opcion.startswith('dehash'):
             #   argumentos = opcion.split(' ')[1:]
              #  comando_dehash = HashCommand()
               # comando_dehash.run(argumentos)
               # time.sleep(3)

            elif opcion.startswith('subdominio'):
                argumentos = opcion.split(' ')[1:]
                comando_dominio = DominioCommand()
                comando_dominio.run(argumentos)
                time.sleep(3)

            elif opcion.startswith('conectar'):
                argumentos = opcion.split(' ')[1:]
                comando_conectart = ConnectCommand()
                comando_conectart.run(argumentos)
                time.sleep(3)

            elif opcion.startswith('lookserver'):
                argumentos = opcion.split(' ')[1:]
                comando_lookserver = LookserverCommand()
                comando_lookserver.run(argumentos)
                time.sleep(3)

            #elif opcion.startswith('scraper'):
             #   argumentos = opcion.split(' ')[1:]
              #  comando_scraper = ScraperCommand()
               # comando_scraper.run(argumentos)
                #time.sleep(3)

            elif opcion.startswith('clientimprovise'):
                mcclient()

            elif opcion == 'close':
                clear_console()
                break

            elif opcion == 'exit':
                clear_console()
                break

            else:
                input(f"""
{R}[{W}x{R}] {R}| {R}Opcion invalida revise {G}/help
""")

                clear_console()
                Letra()
        except Exception as e:
            print(f"Consultar a pablo")

if __name__ == '__main__':
    clear_console()  

    Letra()
    skibidi()