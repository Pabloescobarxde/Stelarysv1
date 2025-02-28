
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
WHITE = "\033[37m"
GRAY = "\033[90m" 

def show_help():
    help_message = f"""
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Help{GRAY}] {GRAY}- [{WHITE}Muestra este mensaje{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Doxing{GRAY}] {GRAY}- [{WHITE}Muestra los comandos de doxing{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Reload{GRAY}] {GRAY}- [{WHITE}Reloadea la tools{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Exit/Close{GRAY}] {GRAY}- [{WHITE}Cierra la tools{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Server{GRAY}] {GRAY}- [{WHITE}Ips:puerto/dominio{GRAY}]{GRAY}-[{WHITE}Informacion De un Servidor De Minecraft{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Check{GRAY}] {GRAY}- [{WHITE}Nicks{GRAY}]{GRAY}-[{WHITE}Te dice si un jugador de Minecraft es premium o No premium{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}IPinfo{GRAY}] {GRAY}- [{WHITE}ips{GRAY}]{GRAY}-[{WHITE}Te da la informacion sobre la IP{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Search{GRAY}] {GRAY}- [{WHITE}Nick{GRAY}]{GRAY}- [{WHITE}Dehash{GRAY}]{GRAY} {GRAY}-[{WHITE}Te da passwords Ips de nickname{GRAY}] [{WHITE}Dehash Al hacer la busqueda te dehashea la passwords automaticamente{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Dehash{GRAY}] {GRAY}- [{WHITE}Hash{GRAY}] [{WHITE}Ruta Multiple Hash{GRAY}]{GRAY}-[{WHITE}Decifras un hash de manera bruta{GRAY}] {GRAY}-[{WHITE}Ruta Hash colocas la ruta con multiple hash lo decifra{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Scan{GRAY}] {GRAY}- [{WHITE}ips{GRAY}]{GRAY}-[{WHITE}Escanea un los puerto de una ip{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Subdominio{GRAY}] {GRAY}- [{WHITE}Dominio{GRAY}]{GRAY}-[{WHITE}Te da todos los dominios, ip relacionado al dominio{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Connect{GRAY}] {GRAY}- [{WHITE}Ip{GRAY}]{GRAY}-[{WHITE}Conecta un bot a un servidor de minecraft{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Lookserver{GRAY}] {GRAY}- [{WHITE}cantidad{GRAY}]{GRAY}-[{WHITE}Te da una lista de servidores para poder raidear{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}CrackConnect{GRAY}] {GRAY}- [{WHITE}Ip{GRAY}]{GRAY}-[{WHITE}Conecta un bot y intenta logearse con fuerza bruta{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}proxy{GRAY}] {GRAY}- [{WHITE}Ip{GRAY}]{GRAY}-[{WHITE}Crea un servidor falso para poder obtener datos{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Openplayer{GRAY}] {GRAY}- [{WHITE}Ip{GRAY}]{GRAY}-[{WHITE}Obtienes todos los nicks de un servidor{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Cliente{GRAY}] {GRAY}- [{WHITE}Abre cliente oficial de {GREEN}Skibidi{WHITE}Grief{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Shodan{GRAY}] {GRAY}- [{WHITE}Ip{GRAY}]{GRAY}-[{WHITE}Obtienes la informacion de la ip atra vez de shodan{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}attackbot{GRAY}] {GRAY}- [{WHITE}Ip{GRAY}]{GRAY}-[{WHITE}Hace un ataque de bots a un servidor{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Scapper{GRAY}] {GRAY}- [{WHITE}Tienda{GRAY}]{GRAY}-[{WHITE}Obtienes toda las ultimas compra de ese servidor{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}DDoS{GRAY}] {GRAY}- [{WHITE}ip{GRAY}]{GRAY}- [{WHITE}Puerto{GRAY}]{GRAY}-[{WHITE}Haces ataques de negacion de servicios{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}logserver{GRAY}] {GRAY}- [{WHITE}Muestra toda las personas que entran a un servidor lo guarda en un .json{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}ClientImprovise{GRAY}] {GRAY}- [{WHITE}Te abre minecraft improvisadamente{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}Grifing{GRAY}] {GRAY}- [{WHITE}Muestra comandos de grifing{GRAY}]
{GRAY}[{GREEN}#{GRAY}] {GRAY}[{WHITE}playerlogs{GRAY}] {GRAY}- [{WHITE}Puedes saber en todos los servidores que esta logeado un jugador{GRAY}]
    """
    print(help_message)

if __name__ == "__main__":
    pass 
