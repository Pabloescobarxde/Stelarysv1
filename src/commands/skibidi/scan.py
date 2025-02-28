import subprocess
import re
import signal
import time
from mccolors import mcwrite

class Command:
    def __init__(self):
        self.name = 'scan'
        self.arguments: list = ['ip_address']

    def validate_arguments(self, arguments: list):
        if len(arguments) == 0:
            return False
        return True    

    def scan_ip(self, ip_address: str, ip_number: int):
        mcwrite(f'&8&l[&a&l+&8&l] &8&l[&f&lEscaneando IP &c{ip_address}&8&l]')
        print("")

        nmap_command = [
            'nmap',
            '-p', '100-150,151-165,166-199,200-250,251-265,266-299,300-350,351-365,366-399,400-450,451-465,466-499,500-550,551-565,566-599,600-650,651-665,666-699,700-750,751-765,766-799,800-850,851-865,866-899,900-950,951-965,966-999,1000-1100,1101-1165,1166-1999,2000-2200,2201-2265,2266-2999,3000-3300,3301-3365,3366-3999,4000-4400,4401-4465,4466-4999,5000-5500,5501-5565,5566-5999,6000-6600,6601-6665,6666-6999,7000-7700,7701-7765,7766-7999,8000-8800,8801-8865,8866-8999,9000-9900,9901-9965,9966-9999,10000-15500,15501-15565,15566-19999,20000-25500,25501-25565,25566-29999,30000-35500,35501-35565,35566-39999,40000-45500,45501-45565,45566-49999,50000-55500,55501-55565,55566-59999,60000-65500,65501-65535',
            '-T5',
            '-A',
            '-v',
            '-Pn',
            '--min-hostgroup', '8',
            '--max-hostgroup', '8',
            ip_address
        ]

        try:
            process = subprocess.Popen(nmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            port_protocol_pattern = re.compile(r'Discovered open port (\d+/\w+) on \d+\.\d+\.\d+\.\d+')

            for line in process.stdout:
                match = port_protocol_pattern.search(line)
                if match:
                    port_protocol = match.group(1)
                    mcwrite(f'&8&l[&c&l#&8&l]&8&l [&f&lPuerto abierto: &a{port_protocol} &fen &c{ip_address}&8&l]')

            process.wait()
            
            mcwrite('')
            mcwrite(f'&8&l[&c&l#&8&l] &8&l[&f&lScan de IP &c{ip_number} &ffinalizado.&8&l]')
            mcwrite('')

        except Exception as e:
            mcwrite('')
            mcwrite(f'&8&l[&c&l#&8&l] &8&l[&f&lError durante el escaneo de &c{ip_address}&f: &c{str(e)}&8&l]')
            mcwrite('')

    def signal_handler(self, signal, frame):
        mcwrite('')
        mcwrite('&8&l[&c&l#&8&l] &8&l[&f&lVolviendo al menú en 5 segundos...&8&l]')
        time.sleep(5)
        return

    def run(self, arguments: list):
        signal.signal(signal.SIGINT, self.signal_handler)

        if not self.validate_arguments(arguments):
            mcwrite('')
            mcwrite('&8&l[&c&l#&8&l] &8&l[&f&lArgumentos invalidos!&8&l] &f- &8&l[&fScan <ip> o <"ruta de archivo">&8&l]')
            return

        mcwrite('')
        mcwrite('&8&l[&a&l+&8&l] &8&l[&f&lComenzando Scan.&8&l]')
        ip_address_input = arguments[0]

        if ip_address_input is None:
            mcwrite('')
            mcwrite('&8&l[&c&l#&8&l] &8&l[&f&lIP Invalida&8&l]')
            return

        if ip_address_input.startswith('"') and ip_address_input.endswith('"'):  
            ip_address_input = ip_address_input[1:-1]

            try:
                with open(ip_address_input, 'r') as file:
                    ip_addresses = [line.strip() for line in file.readlines()]
                mcwrite('&8&l[&c&l#&8&l] &8&l[&f&lEscaneando múltiples IPs desde el archivo...&8&l]')
                for index, ip in enumerate(ip_addresses, start=1):
                    self.scan_ip(ip, index)
            except Exception as e:
                mcwrite('')
                mcwrite(f'&8&l[&c&l#&8&l] &8&l[&f&lError al leer el archivo de IPs: &c{str(e)}&8&l]')
        else:
            self.scan_ip(ip_address_input, 1)
