import time, os

# from src.Utils.discord_estado            import init_discord, update_presence
from src.commands.skibidi.help             import show_help
from src.commands.skibidi.server           import get_server_info
from src.commands.skibidi.ipinfo           import obtener_info_de_ip
from src.commands.skibidi.jugador          import check_premium, get_username_history, display_results
from src.commands.skibidi.shodan           import Command as ShodanCommand
from src.commands.skibidi.scan             import Command as ScanCommand
from src.commands.skibidi.ddos             import Command as DDoSCommand
from src.commands.skibidi.subdominio       import Command as DominioCommand
from src.commands.skibidi.conectar         import Command as ConnectCommand
from src.commands.skibidi.Lookserver       import Command as LookserverCommand
from src.commands.doxxing                  import menu_simplify, doxing
from src.utils.console                     import clear
from MCclient.main                         import mcclient
from colorama                              import init, Fore, Style

init(autoreset=True)

COLORES = {
    "R": Fore.RED,
    "W": Fore.WHITE,
    "GRAY": Fore.LIGHTBLACK_EX,
    "G": Fore.GREEN,
    "P": Fore.MAGENTA
}

PROMPT = f"{COLORES['R']}┌───[root@discord.gg/astralix]\n└──$ {Style.RESET_ALL}"
INVALIDO = f"{COLORES['R']}[{COLORES['W']}x{COLORES['R']}] | Opcion invalida revise {COLORES['G']}/help"

BANNER = f"""
  {COLORES['R']}███████╗████████╗███████╗██╗      █████╗ ██████╗ ██╗   ██╗███████╗           
  {COLORES['R']}██╔════╝╚══██╔══╝██╔════╝██║     ██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝     
  {COLORES['R']}███████╗   ██║   █████╗  ██║     ███████║██████╔╝ ╚████╔╝ ███████╗                                    
  {COLORES['W']}╚════██║   ██║   ██╔══╝  ██║     ██╔══██║██╔══██╗  ╚██╔╝  ╚════██║              
  {COLORES['W']}███████║   ██║   ███████╗███████╗██║  ██║██║  ██║   ██║   ███████║        
  {COLORES['W']}╚══════╝   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝                                       

  {COLORES['GRAY']}[{COLORES['W']}StelarysTool {COLORES['GRAY']}-{COLORES['W']} Comienza con {COLORES['G']} Help{COLORES['GRAY']} {COLORES['R']}By Pablo{COLORES['GRAY']}]
"""

COMANDOS = {
    "help": show_help,
    "doxing": lambda: (clear(), doxing(), menu_simplify()),
    "clear": lambda: (clear(), print(BANNER)),
    "clientimprovise": mcclient,
    "exit": clear,
    "close": clear
}

def Letra():
    print(BANNER)


def execute_command(opcion):
    if opcion in COMANDOS:
        COMANDOS[opcion]()
    
    elif opcion.startswith("check "):
        nickname = opcion.split(" ", 1)[1]
        uuid, status = check_premium(nickname)
        history = get_username_history(uuid) if uuid else None
        display_results(nickname, uuid, status, history)
    
    elif opcion.startswith("ipinfo "):
        ip = opcion.split(" ", 1)[1]
        print(f"URL del Mapa: {obtener_info_de_ip(ip)}")
        
    elif opcion.startswith("server "):
        ip = opcion.split(" ", 1)[1]
        get_server_info(ip)
        
    elif opcion.startswith("shodan"):
        ShodanCommand().run(opcion.split()[1:])
        time.sleep(3)
        
    elif opcion.startswith("scan"):
        ScanCommand().run(opcion.split()[1:])
        time.sleep(3)
        
    elif opcion.startswith("ddos"):
        DDoSCommand().run(opcion.split()[1:])
        time.sleep(3)
        
    elif opcion.startswith("subdominio"):
        DominioCommand().run(opcion.split()[1:])
        time.sleep(3)
        
    elif opcion.startswith("conectar"):
        ConnectCommand().run(opcion.split()[1:])
        time.sleep(3)
        
    elif opcion.startswith("lookserver"):
        LookserverCommand().run(opcion.split()[1:])
        time.sleep(3)
    else:
        print(INVALIDO)


def skibidi():
    global current_menu
    while True:
        opcion = input(INVALIDO)
        try:
            execute_command(opcion)
        except Exception as e:
            print(f"{COLORES['R']}[{COLORES['W']}x{COLORES['R']}] | Hubo un error, consulta en discord.gg/astralix")
        clear()
        Letra()


if __name__ == "__main__":
    clear()
    Letra()
    skibidi()
