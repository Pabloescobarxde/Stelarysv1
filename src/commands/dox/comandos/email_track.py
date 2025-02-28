import requests
from bs4 import BeautifulSoup


GRAY = '\033[90m'
RED = '\033[91m'
GREEN = '\033[92m'
WHITE = '\033[97m'
RESET = '\033[0m'

def Instagram(email):
    try:
        session = requests.Session()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        headers = {
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'es-ES,es;q=0.5',
            'Origin': 'https://www.instagram.com',
            'Connection': 'keep-alive',
            'Referer': 'https://www.instagram.com/'
        }

        data = {
            "email": email
        }

        response = session.get(
            "https://www.instagram.com/accounts/emailsignup/", 
            headers=headers
        )
        if response.status_code == 200:
            if 'csrftoken' in session.cookies:
                token = session.cookies['csrftoken']
            else:
                return f"{GRAY}[{RED}#{GRAY}]{WHITE} Error: Token no encontrado."
        else:
            return f"{GRAY}[{RED}#{GRAY}]{WHITE} Error: {response.status_code}"

        headers["x-csrftoken"] = token
        headers["Referer"] = "https://www.instagram.com/accounts/emailsignup/"

        response = session.post(
            url="https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",
            headers=headers,
            data=data
        )
        if response.status_code == 200:
            if "Another account is using the same email." in response.text:
                return f"{GRAY}[{GREEN}#{GRAY}]{WHITE} Instagram: Encontrado"
            elif "email_is_taken" in response.text:
                return f"{GRAY}[{GREEN}#{GRAY}]{WHITE} Instagram: Encontrado"
            else:
                return f"{GRAY}[{RED}#{GRAY}]{WHITE} Instagram: No encontrado"
        else:
            return f"{GRAY}[{RED}#{GRAY}]{WHITE} Error: {response.status_code}"
    except Exception as e:
        return f"{GRAY}[{RED}#{GRAY}]{WHITE} Error: {e}"

def Twitter(email):
    try:
        session = requests.Session()
        response = session.get(
            url="https://api.twitter.com/i/users/email_available.json",
            params={
                "email": email
            }
        )
        if response.status_code == 200:
            if response.json()["taken"] == True:
                return f"{GRAY}[{GREEN}#{GRAY}]{WHITE} Twitter: Encontrado"
            else:
                return f"{GRAY}[{RED}#{GRAY}]{WHITE} Twitter: No encontrado"
        else:
            return f"{GRAY}[{RED}#{GRAY}]{WHITE} Error: {response.status_code}"
    except Exception as e:
        return f"{GRAY}[{RED}#{GRAY}]{WHITE} Error: {e}"

def PornHub(email):
    try:
        session = requests.Session()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        headers = {
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en,en-US;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

        response = session.get("https://www.pornhub.com/signup", headers=headers)
        if response.status_code == 200:
            token = BeautifulSoup(response.content, features="html.parser").find(attrs={"name": "token"})
            if token is None:
                return f"{GRAY}[{RED}#{GRAY}]{WHITE} PornHub: Error: Token no encontrado."
            token = token.get("value")
        else:
            return f"{GRAY}[{RED}#{GRAY}]{WHITE} PornHub: Error: {response.status_code}"

        params = {
            'token': token,
        }

        data = {
            'check_what': 'email',
            'email': email
        }

        response = session.post(
            'https://www.pornhub.com/user/create_account_check',
            headers=headers,
            params=params,
            data=data
        )
        if response.status_code == 200:
            if response.json().get("error_message") == "Email has been taken.":
                return f"{GRAY}[{GREEN}#{GRAY}]{WHITE} PornHub: Encontrado"
            elif "Email has been taken." in response.text:
                return f"{GRAY}[{GREEN}#{GRAY}]{WHITE} PornHub: Encontrado"
            else:
                return f"{GRAY}[{RED}#{GRAY}]{WHITE} PornHub: No encontrado"
        else:
            return f"{GRAY}[{RED}#{GRAY}]{WHITE} PornHub: Error: {response.status_code}"
    except Exception as e:
        return f"{GRAY}[{RED}#{GRAY}]{WHITE} PornHub: Error: {e}"

        
        
def Spotify(email):
    try:
        session = requests.Session()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        headers = {
            'User-Agent': user_agent,
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
        }
        
        params = {
            'validate': '1',
            'email': email,
        }

        response = session.get(
            'https://spclient.wg.spotify.com/signup/public/v1/account',
            headers=headers,
            params=params
        )
        if response.status_code == 200:
            if response.json()["status"] == 1:
                return f"{GRAY}[{RED}#{GRAY}]{WHITE} Spotify: No encontrado"
            elif response.json()["status"] == 20:
                return f"{GRAY}[{GREEN}#{GRAY}]{WHITE} Spotify: Encontrado"
            else:
                return f"{GRAY}[{RED}#{GRAY}]{WHITE} Spotify: No encontrado"
        else:
            return f"{GRAY}[{RED}#{GRAY}]{WHITE} Error: {response.status_code}"
    except Exception as e:
        return f"{GRAY}[{RED}#{GRAY}]{WHITE} Error: {e}"

def Xnxx(email):
    try:
        session = requests.Session()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        headers = {
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-en',
            'Host': 'www.xnxx.com',
            'Referer': 'https://www.google.com/',
            'Connection': 'keep-alive'
        }

       
        cookie = session.get('https://www.xnxx.com', headers=headers)
        if cookie.status_code == 200:
            if not cookie.cookies:
                return f"{GRAY}[{RED}#{GRAY}]{WHITE} Xnxx: Error: Cookie no encontrada."
        else:
            return f"{GRAY}[{RED}#{GRAY}]{WHITE} Xnxx: Error: {cookie.status_code}"

        
        headers['Referer'] = 'https://www.xnxx.com/video-holehe/palenath_fucks_xnxx_with_holehe'
        headers['X-Requested-With'] = 'XMLHttpRequest'
        email_encoded = email.replace('@', '%40')

        response = session.get(
            f'https://www.xnxx.com/account/checkemail?email={email_encoded}',
            headers=headers,
            cookies=cookie.cookies
        )

        if response.status_code == 200:
            try:
                json_response = response.json()
                if json_response.get('message') == "This email is already in use or its owner has excluded it from our website.":
                    return f"{GRAY}[{GREEN}#{GRAY}]{WHITE} Xnxx: Encontrado"
                elif json_response.get('message') == "Invalid email address.":
                    return f"{GRAY}[{RED}#{GRAY}]{WHITE} Xnxx: No encontrado"
                elif json_response.get('result') == "false" or json_response.get('code') == 1:
                    return f"{GRAY}[{GREEN}#{GRAY}]{WHITE} Xnxx: Encontrado"
                elif json_response.get('result') == "true" or json_response.get('code') == 0:
                    return f"{GRAY}[{RED}#{GRAY}]{WHITE} Xnxx: No encontrado"
            except Exception:
                return f"{GRAY}[{RED}#{GRAY}]{WHITE} Xnxx: Error en la respuesta del servidor."
        else:
            return f"{GRAY}[{RED}#{GRAY}]{WHITE} Xnxx: Error: {response.status_code}"
    except Exception as e:
        return f"{GRAY}[{RED}#{GRAY}]{WHITE} Xnxx: Error: {e}"

def Xvideo(email):
    try:
        session = requests.Session()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        headers = {
            'User-Agent': user_agent,
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Referer': 'https://www.xvideos.com/',
        }

        params = {
            'email': email,
        }

        response = session.get('https://www.xvideos.com/account/checkemail', headers=headers, params=params)
        if response.status_code == 200:
            try:
                json_response = response.json()
                if json_response.get('message') == "This email is already in use or its owner has excluded it from our website.":
                    return f"{GRAY}[{GREEN}#{GRAY}]{WHITE} Xvideo: Encontrado"
                elif json_response.get('message') == "Invalid email address.":
                    return f"{GRAY}[{RED}#{GRAY}]{WHITE} Xvideo: No encontrado"
                elif json_response.get('result') == "false" or json_response.get('code') == 1:
                    return f"{GRAY}[{GREEN}#{GRAY}]{WHITE} Xvideo: Encontrado"
                elif json_response.get('result') == "true" or json_response.get('code') == 0:
                    return f"{GRAY}[{RED}#{GRAY}]{WHITE} Xvideo: No encontrado"
                else:
                    return f"{GRAY}[{RED}#{GRAY}]{WHITE} Xvideo: Respuesta desconocida"
            except Exception:
                return f"{GRAY}[{RED}#{GRAY}]{WHITE} Xvideo: Error al procesar la respuesta del servidor."
        else:
            return f"{GRAY}[{RED}#{GRAY}]{WHITE} Xvideo: Error HTTP: {response.status_code}"
    except Exception as e:
        return f"{GRAY}[{RED}#{GRAY}]{WHITE} Xvideo: Error: {e}"

def Pinterest(email):
    try:
        session = requests.Session()
        response = session.get(
            "https://www.pinterest.com/_ngjs/resource/EmailExistsResource/get/",
            params={
                "source_url": "/",
                "data": '{"options": {"email": "' + email + '"}, "context": {}}'
            }
        )

        if response.status_code == 200:
            try:
                json_response = response.json()
                message = json_response.get("resource_response", {}).get("message")
                data = json_response.get("resource_response", {}).get("data")

                if message == "Invalid email.":
                    return f"{GRAY}[{RED}#{GRAY}]{WHITE} Pinterest: No encontrado"
                elif message == "ok":
                    if data is False:
                        return f"{GRAY}[{RED}#{GRAY}]{WHITE} Pinterest: No encontrado"
                    elif data is True:
                        return f"{GRAY}[{GREEN}#{GRAY}]{WHITE} Pinterest: Encontrado"
                    else:
                        return f"{GRAY}[{RED}#{GRAY}]{WHITE} Pinterest: Respuesta desconocida"
                else:
                    return f"{GRAY}[{RED}#{GRAY}]{WHITE} Pinterest: Respuesta desconocida"
            except Exception:
                return f"{GRAY}[{RED}#{GRAY}]{WHITE} Pinterest: Error al procesar la respuesta del servidor."
        else:
            return f"{GRAY}[{RED}#{GRAY}]{WHITE} Pinterest: Error HTTP: {response.status_code}"
    except Exception as e:
        return f"{GRAY}[{RED}#{GRAY}]{WHITE} Pinterest: Error: {e}"


def email_track():
    try:
        email = input(f"\n{GRAY}[{RED}#{GRAY}]{WHITE} Introduce un correo electrónico: ")
        print(f"")

        sites = [
            Instagram, Twitter, Spotify, Pinterest, PornHub, Xnxx, Xvideo
        ]

        site_founds = []
        found = 0
        not_found = 0
        error = 0

        for site in sites:
            result = site(email)
            print(result)
            if "Encontrado" in result:
                site_founds.append(site.__name__)
                found += 1
            elif "No encontrado" in result:
                not_found += 1
            else:
                error += 1

        if found != 0:
            print(f"\n{GRAY}[{GREEN}#{GRAY}]{WHITE} Total Encontrado: {found}   {GRAY}[{RED}#{GRAY}]{WHITE} No encontrado: {not_found}")
            print("")
    except Exception as e:
        print(f"{GRAY}[{RED}#{GRAY}]{WHITE} Consultar Pablo")

if __name__ == "__main__":
    email_track()
