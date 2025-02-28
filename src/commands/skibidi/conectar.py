import subprocess
import time
import re
import os
from mccolors import mcwrite


class Command:
    def __init__(self):
        self.name = 'connect'
        self.arguments: list = ['nick', 'ip', 'port']

        # Calcula la raíz del proyecto correctamente
        self.project_root = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..', '..')
        )
        self.script_path = os.path.join(
            self.project_root, 'conexiones', 'connect', 'bot.js'
        )

    def validate_arguments(self, arguments: list):
        if len(arguments) != len(self.arguments):
            return False

        # Validar IP
        if not re.match(r'^(\d{1,3}\.){3}\d{1,3}$', arguments[1]):
            return False

        # Validar puerto
        if not arguments[2].isdigit() or not (0 <= int(arguments[2]) <= 65535):
            return False

        # Validar nick
        if not arguments[0].isalnum() or len(arguments[0]) > 16:
            return False

        return True

    def run(self, arguments: list):
        if not self.validate_arguments(arguments):
            mcwrite('')
            mcwrite(' &f- &8&l[&fArgumento inválido!&8] &f- &8[&fUsa: connect <nick> <ip> <puerto> <Version>&8]')
            mcwrite('')
            time.sleep(3)
            return

        # Verificar si el archivo existe antes de ejecutar
        if not os.path.exists(self.script_path):
            mcwrite('')
            mcwrite(f' &f- &8&l[&fError: No se encontró el archivo: {self.script_path}&8]')
            mcwrite('')
            time.sleep(3)
            return

        # Conectar al servidor usando Node.js
        try:
            subprocess.run(
                ['node', self.script_path, arguments[0], arguments[1], arguments[2]],
                check=True
            )
        except subprocess.CalledProcessError as e:
            mcwrite('')
            mcwrite(f' &f- &8&l[&fError al ejecutar el comando: {e}&8]')
            mcwrite('')
            time.sleep(2)
