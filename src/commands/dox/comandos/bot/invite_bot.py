import webbrowser
from colorama import Fore, Style, init

init(autoreset=True)


def ErrorId():
    print(f"\n{Fore.GRAY}[{Fore.RED}#{Fore.GRAY}]{Fore.WHITE} La id del bot es invalida")

def Error(e):
    print(f"\n{Fore.GRAY}[{Fore.RED}#{Fore.GRAY}]{Fore.WHITE} error invalido")


def invite_bot_id():
    try:
        try:
            IdBot = int(input(f"\n{Fore.GRAY}[{Fore.GREEN}#{Fore.GRAY}]{Fore.WHITE} Proporcione la ID del bot: "))
        except ValueError:
            ErrorId()

        url_invitacion = f'https://discord.com/oauth2/authorize?client_id={IdBot}&scope=bot&permissions=8'
        print(f"\n{Fore.GRAY}[{Fore.RED}#{Fore.GRAY}]{Fore.WHITE} URL de invitación: {Fore.GRAY}[{Fore.WHITE}{url_invitacion}{Fore.GRAY}]")

        eleccion = input(f"\n{Fore.GRAY}[{Fore.GREEN}#{Fore.GRAY}]{Fore.WHITE} Deseas abrir el navegador (s/n) ")
        if eleccion.lower() in ['s', 'si']:
            webbrowser.open_new_tab(url_invitacion)

    except Exception as e:
        Error(e)

if __name__ == "__main__":
    pass
