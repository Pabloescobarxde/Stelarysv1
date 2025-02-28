## Ya no funcional le pusieron cludflare:(


import os
import json
import random
import requests
from bs4 import BeautifulSoup


RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
WHITE = "\033[37m"
GRAY = "\033[90m"

class Command:
    def __init__(self):
        self.name = 'Lookserver' 
        self.arguments = ['Lookserver, modalidad, cuanto servidores'] 
        self.found_domains = set()
        self.results = []

    def apply_minecraft_colors(self, text):
        colors = {
            
        }
        for code, color in colors.items():
            text = text.replace(code, color)
        return text

    def get_server_info(self, ip, server_number, online_count, offline_count):
        response = requests.get(f"https://api.mcsrvstat.us/3/{ip}")
        server_data = response.json()

        if response.status_code != 200 or not server_data.get('online'):
            offline_count += 1
            print(f"""
{GRAY}[{RED}✘{GRAY}]{GRAY} El servidor {ip} está fuera de línea.
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Server Numero{GRAY}] {GRAY}- [{RED}{server_number}{GRAY}]
            """)
            return online_count, offline_count, None

        ip_port = f"{server_data.get('ip')}:{server_data.get('port')}"
        motd = self.apply_minecraft_colors("\n".join(server_data.get('motd', {}).get('clean', [])))
        version = server_data.get('version')
        protocol = server_data.get('protocol')
        players = server_data.get('players', {}).get('online', 0)
        max_players = server_data.get('players', {}).get('max', 0)
        mods = server_data.get('mods', {}).get('names', [])
        software = server_data.get('software', 'Desconocido')

        print(f"""
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Ip:Puerto{GRAY}] {GRAY}- [{RED}{ip_port}{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Motd{GRAY}] {GRAY}- [{RED}{motd}{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Version{GRAY}] {GRAY}- [{RED}{version}{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Protocolo{GRAY}] {GRAY}- [{RED}{protocol}{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Jugadores{GRAY}] {GRAY}- [{RED}{players}{GRAY}] [{RED}{max_players}{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Mods{GRAY}] {GRAY}- [{RED}{mods}{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Server Hecho{GRAY}] {GRAY}- [{RED}{software}{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} [{WHITE}Server Numero{GRAY}] {GRAY}- [{RED}{server_number}{GRAY}]
        """)

        server_info = {
            "ip_port": ip_port,
            "motd": motd,
            "version": version,
            "protocol": protocol,
            "players": {
                "online": players,
                "max": max_players
            },
            "mods": mods,
            "software": software,
            "server_number": server_number
        }

        online_count += 1
        return online_count, offline_count, server_info

    def obtener_ips(self, modalidad, pagina):
        url = f"https://minecraftservers.org/search/{modalidad}/{pagina}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"{RED}Consultar a pablo")
            return []
        
        soup = BeautifulSoup(response.text, "html.parser")
        server_listings = soup.find_all('div', class_='server-listing')
        
        ips = []
        for server in server_listings:
            ip = server.find('div', class_='url').text.strip()
            ips.append(ip)
        
        return ips

    def obtener_ips_totales(self, modalidad, cantidad):
        ips_totales = []
        pagina = 1
        
        while len(ips_totales) < cantidad:
            ips = self.obtener_ips(modalidad, pagina)
            if not ips:
                break
            ips_totales.extend(ips)
            if len(ips_totales) >= cantidad:
                break
            pagina += 1
        
        return ips_totales[:cantidad]

    def obtener_servidores(self, modalidad, cantidad, guardar):
        print(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Buscando servidores {modalidad}...")
        ips = self.obtener_ips_totales(modalidad, cantidad)
        
        online_count = 0
        offline_count = 0
        servidores = []

        for idx, ip in enumerate(ips, 1):
            online_count, offline_count, server_info = self.get_server_info(ip, idx, online_count, offline_count)
            if server_info:
                servidores.append(server_info)

        print(f"{GRAY}[{GREEN}✓{GRAY}]{WHITE} Servidores online: {online_count}")
        print(f"{GRAY}[{RED}×{GRAY}]{GRAY} Servidores offline {WHITE}{offline_count}")
        print(f"")

        if guardar:
            self.guardar_servidores(modalidad, servidores)

    def guardar_servidores(self, modalidad, servidores):
        if not os.path.exists("servidores"):
            os.makedirs("servidores")

        random_number = random.randint(1000, 9999)
        file_name = f"servidores/{modalidad}_{random_number}.json"

        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(servidores, file, ensure_ascii=False, indent=4)

    def run(self, argumentos):
        if len(argumentos) > 1:
            modalidad = argumentos[0]
            cantidad = int(argumentos[1])
            guardar = input(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} ¿Deseas guardar la búsqueda de datos? (s/n): ").strip().lower() == 's'
            self.obtener_servidores(modalidad, cantidad, guardar)
        else:
            print(f"\n{GRAY}[{RED}x{GRAY}]{WHITE} Por favor usar lookserver <modalidad> <cuanto servidores>")
