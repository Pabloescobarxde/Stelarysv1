import urllib.request
import urllib.parse
import re
import socket
from datetime import datetime
import concurrent.futures
from colorama import init, Fore, Style
import whois
import requests
import dns.resolver

RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
WHITE = "\033[37m"
GRAY = "\033[90m"
BLUE = "\033[34m"

init(autoreset=True)

class Command:
    def __init__(self):
        self.name = 'subdominio'
        self.arguments = ['subdominio']
        self.found_domains = set()
        self.results = []

    def obtener_ip(self, dominio):
        try:
            ip = socket.gethostbyname(dominio)
            return ip
        except:
            return "No disponible"

    def obtener_info_whois(self, dominio):
        try:
            w = whois.whois(dominio)
            return {
                'registrar': w.registrar,
                'creation_date': w.creation_date,
                'expiration_date': w.expiration_date
            }
        except:
            return None

    def verificar_https(self, dominio):
        try:
            requests.get(f"https://{dominio}", timeout=5, verify=False)
            return True
        except:
            return False

    def obtener_registros_dns(self, dominio):
        registros = {}
        tipos = ['A', 'MX', 'NS', 'TXT']
        
        for tipo in tipos:
            try:
                answers = dns.resolver.resolve(dominio, tipo)
                registros[tipo] = [str(rdata) for rdata in answers]
            except:
                registros[tipo] = []
                
        return registros

    def escanear_subdominio(self, subdominio):
        ip = self.obtener_ip(subdominio)
        https = self.verificar_https(subdominio)
        registros_dns = self.obtener_registros_dns(subdominio)
        
        return {
            'subdominio': subdominio,
            'ip': ip,
            'https': https,
            'registros_dns': registros_dns
        }

    def escanear_subdominios(self, domain):
        print(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Iniciando escaneo completo para: {domain}")
        print(f"{GRAY}[{RED}-{GRAY}]{WHITE} Tiempo de inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        try:
            whois_info = self.obtener_info_whois(domain)
            if whois_info:
                print(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Información del dominio principal:")
                print(f"{GRAY}[{RED}-{GRAY}] {WHITE} Registrado {whois_info['registrar']}")
                print(f"{GRAY}[{RED}-{GRAY}] {WHITE} Fecha de creación: {whois_info['creation_date']}")
                print(f"{GRAY}[{RED}-{GRAY}] {WHITE} Fecha de expiración: {whois_info['expiration_date']}")

            url = 'https://crt.sh/?q=' + urllib.parse.quote('%.' + domain)
            with urllib.request.urlopen(url) as r:
                code = r.read().decode('utf-8')
                pattern = re.compile(r'<tr>(?:\s|\S)*?href="\?id=([0-9]+?)"(?:\s|\S)*?<td>([*_a-zA-Z0-9.-]+?\.' + re.escape(domain) + r')</td>(?:\s|\S)*?</tr>', re.IGNORECASE)
                
                subdominios = set()
                for cert, subdominio in pattern.findall(code):
                    subdominios.add(subdominio.split('@')[-1])

                print(f"\n{GRAY}[{GREEN}+{GRAY}]{WHITE} Encontrados {len(subdominios)} subdominios únicos")
                
                with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                    futures = [executor.submit(self.escanear_subdominio, subdominio) for subdominio in subdominios]
                    
                    for future in concurrent.futures.as_completed(futures):
                        result = future.result()
                        subdominio = result['subdominio']
                        ip = result['ip']
                        https = result['https']
                        registros_dns = result['registros_dns']
                        
                        print(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Subdominio: {subdominio}")
                        print(f"{GRAY}[{RED}-{GRAY}]{WHITE} IP: {ip}")
                        print(f"{GRAY}[{RED}-{GRAY}]{WHITE} HTTPS: {'Sí' if https else 'No'}")
                        print(f"{GRAY}[{RED}-{GRAY}]{WHITE} Registros DNS:")
                        for tipo, registros in registros_dns.items():
                            if registros:
                                print(f"{GRAY}{WHITE} {tipo}: {', '.join(registros)}")

            print(f"\n{GRAY}[{GREEN}✓{GRAY}]{WHITE} Escaneo completado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        except Exception as e:
            print(f"\n{GRAY}[{RED}x{GRAY}]{WHITE} Error durante el escaneo:")

    def run(self, argumentos):
        if len(argumentos) > 0:
            domain = argumentos[0]
            self.escanear_subdominios(domain)
        else:
            print(f"\n{GRAY}[{RED}x{GRAY}]{WHITE} No se proporcionó un dominio.")
