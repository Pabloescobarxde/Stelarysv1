import requests

GRAY = "\033[90m"
WHITE = "\033[97m"
RED = "\033[91m"

def check_premium(nickname):
    api_url = f"https://api.mojang.com/users/profiles/minecraft/{nickname}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        uuid = data.get('id')
        return uuid, "premium"
    except requests.exceptions.RequestException:
        return None, "no premium"

def get_username_history(uuid):

    if not uuid:
        return None

    url = f'https://laby.net/api/v3/user/{uuid}/profile'
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        data = response.json()

        if 'name_history' in data:
            
            history = [entry['name'] for entry in data['name_history']]
            return history
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al solicitar datos de la API: {e}")
        return None

def display_results(nickname, uuid, status, history):
    if status == "no premium":
        uuid = "None"
        history = None

        result = f"""
{GRAY}[{RED}#{GRAY}]{GRAY} {GRAY}- [{WHITE}Nickname{GRAY}] {GRAY}- [{RED}{nickname}{GRAY}]       
{GRAY}[{RED}#{GRAY}]{GRAY} {GRAY}- [{WHITE}Status{GRAY}] {GRAY}- [{RED}No premium{GRAY}]    
{GRAY}[{RED}#{GRAY}]{GRAY} {GRAY}- [{WHITE}UUID{GRAY}] {GRAY}- [{RED}None{GRAY}]  
{GRAY}[{RED}#{GRAY}]{GRAY} {GRAY}- [{WHITE}Historial nicks{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} {GRAY}- {GRAY}[{WHITE}none{GRAY}]
        """
        print(result)
    else:
        name_history = "none"
        if history:
            name_history = ", ".join(f"[{name}]" for name in history)

        # salida
        result = f"""
{GRAY}[{RED}#{GRAY}]{GRAY} {GRAY}- [{WHITE}Nickname{GRAY}] {GRAY}- [{RED}{nickname}{GRAY}]       
{GRAY}[{RED}#{GRAY}]{GRAY} {GRAY}- [{WHITE}Status{GRAY}] {GRAY}- [{RED}{status.capitalize()}{GRAY}]    
{GRAY}[{RED}#{GRAY}]{GRAY} {GRAY}- [{WHITE}UUID{GRAY}] {GRAY}- [{RED}{uuid}{GRAY}]  
{GRAY}[{RED}#{GRAY}]{GRAY} {GRAY}- [{WHITE}Historial nicks{GRAY}]
{GRAY}[{RED}#{GRAY}]{GRAY} {RED}- {GRAY}[{WHITE}{name_history}{GRAY}]
        """
        print(result)

