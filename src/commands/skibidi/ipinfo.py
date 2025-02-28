import requests
import subprocess
import socket
import concurrent.futures
import colorama
import sys

RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
WHITE = "\033[37m"
GRAY = "\033[90m"


colorama.init()


class Colores:
    ROJO = colorama.Fore.RED
    BLANCO = colorama.Fore.WHITE
    RESET = colorama.Style.RESET_ALL

def mostrar_error(e):
    print(f"{Colores.ROJO}Error: {e}{Colores.RESET}")

def mostrar_mensaje(mensaje):
    print(mensaje)

def verificar_ping(ip):
    try:
        if sys.platform.startswith("win"):
            resultado = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=1)
        elif sys.platform.startswith("linux"):
            resultado = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=1)
        if resultado.returncode == 0:
            ping = "Éxito"
        else:
            ping = "Fallido"
    except:
        ping = "Fallido"

    print(f"    {Colores.BLANCO}Ping          : {ping}{Colores.RESET}")

def verificar_puertos(ip):
    puertos_abiertos = []

    def escanear_puerto(ip, puerto):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            resultado = sock.connect_ex((ip, puerto))
            if resultado == 0:
                puertos_abiertos.append(puerto)
            sock.close()
        except:
            pass

    with concurrent.futures.ThreadPoolExecutor() as ejecutor:
        resultados = {ejecutor.submit(escanear_puerto, ip, puerto): puerto for puerto in range(1, 1000 + 1)}
    concurrent.futures.wait(resultados)

    print(f"    {Colores.ROJO}Puertos Abiertos: {puertos_abiertos}{Colores.RESET}")

def obtener_dns(ip):
    try:
        dns, aliaslist, ipaddrlist = socket.gethostbyaddr(ip)
    except:
        dns = "Ninguno"
    print(f"    {Colores.BLANCO}DNS           : {dns}{Colores.RESET}")

def obtener_info_ip(ip):
    try:
        respuesta = requests.get(f"https://api.ipapi.com/api/{ip}?access_key=YOUR_ACCESS_KEY")
        api = respuesta.json()

        
        info = {
            "ip": api['ip'],
            "estado": api['status'],
            "pais": api['country_name'],
            "codigo_pais": api['country_code'],
            "region": api['region_name'],
            "codigo_region": api['region_code'],
            "codigo_postal": api['zip'],
            "ciudad": api['city'],
            "latitud": api['latitude'],
            "longitud": api['longitude'],
            "zona_horaria": api['time_zone']['id'],
            "isp": api['org'],
            "org": api['org'],
            "as_host": api['as']['organization'],
        }
    except:
        respuesta = requests.get(f"http://ip-api.com/json/{ip}")
        api = respuesta.json()

        info = {
            "estado": "Inválido" if api['status'] != "success" else "Válido",
            "pais": api.get('country', "Ninguno"),
            "codigo_pais": api.get('countryCode', "Ninguno"),
            "region": api.get('regionName', "Ninguno"),
            "codigo_region": api.get('region', "Ninguno"),
            "codigo_postal": api.get('zip', "Ninguno"),
            "ciudad": api.get('city', "Ninguno"),
            "latitud": api.get('lat', "Ninguno"),
            "longitud": api.get('lon', "Ninguno"),
            "zona_horaria": api.get('timezone', "Ninguno"),
            "isp": api.get('isp', "Ninguno"),
            "org": api.get('org', "Ninguno"),
            "as_host": api.get('as', "Ninguno"),
        }

    mostrar_mensaje(f"""
{GRAY}[{RED}#{GRAY}]{WHITE} Estado        {RED}: {GREEN}{info['estado']}{WHITE}
{GRAY}[{RED}#{GRAY}]{WHITE} País          {RED}: {GREEN}{info['pais']} ({info['codigo_pais']}){WHITE}
{GRAY}[{RED}#{GRAY}]{WHITE} Región        {RED}: {GREEN}{info['region']} ({info['codigo_region']}){WHITE}
{GRAY}[{RED}#{GRAY}]{WHITE} Código Postal {RED}: {GREEN}{info['codigo_postal']}{WHITE}
{GRAY}[{RED}#{GRAY}]{WHITE} Ciudad        {RED}: {GREEN}{info['ciudad']}{WHITE}
{GRAY}[{RED}#{GRAY}]{WHITE} Latitud       {RED}: {GREEN}{info['latitud']}{WHITE}
{GRAY}[{RED}#{GRAY}]{WHITE} Longitud      {RED}: {GREEN}{info['longitud']}{WHITE}
{GRAY}[{RED}#{GRAY}]{WHITE} Zona Horaria  {RED}: {GREEN}{info['zona_horaria']}{WHITE}
{GRAY}[{RED}#{GRAY}]{WHITE} ISP           {RED}: {GREEN}{info['isp']}{WHITE}
{GRAY}[{RED}#{GRAY}]{WHITE} Organización  {RED}: {GREEN}{info['org']}{WHITE}
{GRAY}[{RED}#{GRAY}]{WHITE} AS            {RED}: {GREEN}{info['as_host']}{WHITE}
    """)


def obtener_info_de_ip(ip):
    print(f"\n    {Colores.BLANCO}IP            : {ip}{Colores.RESET}")
    verificar_ping(ip)
    obtener_dns(ip)
    url_mapa = obtener_info_ip(ip)
    verificar_puertos(ip)
    print()

