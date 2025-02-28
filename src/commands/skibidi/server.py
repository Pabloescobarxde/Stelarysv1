import requests

RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
WHITE = "\033[37m"
GRAY = "\033[90m"

def apply_minecraft_colors(text):
    colors = {
    }
    for code, color in colors.items():
        text = text.replace(code, color)
    return text

def get_server_info(ip):
    response = requests.get(f"https://api.mcsrvstat.us/3/{ip}")
    server_data = response.json()

    if response.status_code != 200 or not server_data.get('online'):
        print(f"""

{GRAY}[{RED}✘{GRAY}]{GRAY} El servidor está fuera de línea o no se pudo obtener la información.

           """)
        return

    ip_port = f"{server_data.get('ip')}:{server_data.get('port')}"
    motd = apply_minecraft_colors("\n".join(server_data.get('motd', {}).get('clean', [])))
    version = server_data.get('version')
    protocol = server_data.get('protocol')
    players = server_data.get('players', {}).get('online', 0)
    max_players = server_data.get('players', {}).get('max', 0)
    mods = server_data.get('mods', {}).get('names', [])
    software = server_data.get('software', 'Desconocido')
    ping = server_data.get('debug', {}).get('ping', 'N/A')

    print(f"""
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Ip:Puerto{GRAY}] {GRAY}- [{RED}{ip_port}{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Motd{GRAY}] {GRAY}- [{RED}{motd}{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Version{GRAY}] {GRAY}- [{RED}{version}{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Protocolo{GRAY}] {GRAY}- [{RED}{protocol}{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Jugadores{GRAY}] {GRAY}- [{RED}{players}{GRAY}] [{RED}{max_players}{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Mods{GRAY}] {GRAY}- [{RED}{mods}{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Server Hecho{GRAY}] {GRAY}- [{RED}{software}{GRAY}]
           """)

if __name__ == "__main__":
    pass
