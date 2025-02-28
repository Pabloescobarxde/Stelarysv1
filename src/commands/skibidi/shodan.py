import requests
import socket
from mccolors import mcwrite

class Command:
    def __init__(self):
        self.name = 'shodan'
        self.arguments: list = ['ip o dominio']

    def validate_arguments(self, arguments: list):
        return len(arguments) > 0

    def get_ip(self, target):
        try:
            socket.inet_aton(target)
            return target
        except socket.error:
            try:
                return socket.gethostbyname(target)
            except socket.error:
                return None

    def run(self, arguments: list):
        if not self.validate_arguments(arguments):
            mcwrite("")
            mcwrite(" &f&l- &8&l[&f&lArgumentos inválidos!&8&l] &f- &8&l[&fshodan <ip/dominio>&8&l]")
            return

        target = arguments[0]
        mcwrite("")
        mcwrite(f"&8&l[&a&l+&8&l] &8&l[&f&lBuscando información para: &c{target}&8&l]")

        ip_address = self.get_ip(target)

        if ip_address is None:
            mcwrite("")
            mcwrite(" &f&l- &8&l[&f&lNo se pudo resolver la dirección IP del objetivo.&8&l]")
            return

        internetdb_url = f"https://internetdb.shodan.io/{ip_address}"
        response = requests.get(internetdb_url)

        mcwrite("")
        if response.status_code == 200:
            data = response.json()

            mcwrite(f"&8&l[&a&l#&8&l] &8&l[&f&lInformación de Shodan&8&l]&f:")
            mcwrite(f"&8&l[&a&l#&8&l] &8&l[&fIP&8&l] &f- &8&l[&c{data['ip']}&8&l]")
            mcwrite(f"&8&l[&a&l#&8&l] &8&l[&fHostnames&8&l] &f- &8&l[&c{', '.join(data['hostnames']) if data['hostnames'] else 'N/A'}&8&l]")
            mcwrite(f"&8&l[&a&l#&8&l] &8&l[&fPuertos&8&l] &f- &8&l[&c{', '.join(map(str, data['ports'])) if data['ports'] else 'N/A'}&8&l]")
            mcwrite(f"&8&l[&a&l#&8&l] &8&l[&fVulnerabilidades&8&l] &f- &8&l[&c{', '.join(data['vulns']) if data['vulns'] else 'N/A'}&8&l]")
            mcwrite(f"&8&l[&a&l#&8&l] &8&l[&fCPEs&8&l] &f- &8&l[&c{', '.join(data['cpes']) if data['cpes'] else 'N/A'}&8&l]")
            mcwrite(f"&8&l[&a&l#&8&l] &8&l[&fEtiquetas&8&l] &f- &8&l[&c{', '.join(data['tags']) if data['tags'] else 'N/A'}&8&l]")

        else:
            mcwrite("")
            mcwrite(" &f&l- &8&l[&f&lError al consultar InternetDB, por favor verifica la dirección.&8&l]")

        ipinfo_url = f"https://ipinfo.io/{ip_address}/json"
        ipinfo_response = requests.get(ipinfo_url)

        mcwrite("")
        if ipinfo_response.status_code == 200:
            ipinfo_data = ipinfo_response.json()
            mcwrite("&8&l[&4&l#&8&l] &8&l[&f&lInformación de IPInfo&8&l]&f:")
            mcwrite(f"&8&l[&4&l#&8&l] &8&l[&fIP&8&l] &f- &8&l[&c{ipinfo_data.get('ip', 'N/A')}&8&l]")
            mcwrite(f"&8&l[&4&l#&8&l] &8&l[&fCiudad&8&l] &f- &8&l[&c{ipinfo_data.get('city', 'N/A')}&8&l]")
            mcwrite(f"&8&l[&4&l#&8&l] &8&l[&fRegión&8&l] &f- &8&l[&c{ipinfo_data.get('region', 'N/A')}&8&l]")
            mcwrite(f"&8&l[&4&l#&8&l] &8&l[&fPaís&8&l] &f- &8&l[&c{ipinfo_data.get('country', 'N/A')}&8&l]")
            mcwrite(f"&8&l[&4&l#&8&l] &8&l[&fCódigo postal&8&l] &f- &8&l[&c{ipinfo_data.get('postal', 'N/A')}&8&l]")
            mcwrite(f"&8&l[&4&l#&8&l] &8&l[&fUbicación&8&l] &f- &8&l[&c{ipinfo_data.get('loc', 'N/A')}&8&l]")
            mcwrite(f"&8&l[&4&l#&8&l] &8&l[&fOrganización&8&l] &f- &8&l[&c{ipinfo_data.get('org', 'N/A')}&8&l]")
        else:
            mcwrite("")
            mcwrite(" &f&l- &8&l[&f&lError al obtener información de IPInfo.&8&l]")

        mcwrite("")
