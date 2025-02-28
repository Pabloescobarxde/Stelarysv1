import sys
import datetime

def obtener_fecha_actual():
    now = datetime.datetime.now()
    return now.strftime('%d/%m/%Y')

def set_terminal_title(title):
    sys.stdout.write(f"\033]0;{title}\007")
    sys.stdout.flush()

fecha_actual = obtener_fecha_actual()
