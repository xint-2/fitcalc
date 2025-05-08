from colorama import init, Fore

init()

def print_red(text):
    print(Fore.RED + f"{text}" + Fore.RESET)

def print_green(text):
    print(Fore.GREEN + f"{text}" + Fore.RESET)

def print_blue(text):
    print(Fore.BLUE + f"{text}" + Fore.RESET)

def print_cyan(text):
    print(Fore.CYAN + f"{text}" + Fore.RESET)

def print_magenta(text):
    print(Fore.MAGENTA + f"{text}" + Fore.RESET)

def print_yellow(text):
    print(Fore.YELLOW + f"{text}" + Fore.RESET)
