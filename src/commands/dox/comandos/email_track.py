import subprocess
from colorama import init, Fore

def run_holehe(email):
    try:
        result = subprocess.run(["holehe", email], capture_output=True, text=True, check=True)
        output = result.stdout
        
        for line in output.split("\n"):
            if "[+]" in line:
                print(Fore.GREEN + line)
            elif "[-]" in line:
                print(Fore.RED + line)
            else:
                print(Fore.WHITE + line)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + "Error ejecutando holehe:", e)
    finally:
        print(Fore.RESET)

if __name__ == "__main__":
    init(autoreset=True)
    email = input(f"\n{Fore.LIGHTBLACK_EX}[{Fore.RED}#{Fore.LIGHTBLACK_EX}]{Fore.WHITE} Introduce un correo electrónico: ")
    run_holehe(email)
