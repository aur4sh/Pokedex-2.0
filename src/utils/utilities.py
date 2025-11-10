import os

def limpar():
    baseSystem = os.name

    if baseSystem == 'nt':
        os.system('cls')
    elif baseSystem == 'posix':
        os.system('clear')