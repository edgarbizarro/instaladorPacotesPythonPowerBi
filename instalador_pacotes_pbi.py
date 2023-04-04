import subprocess
import sys

# Lista de pacotes a serem instalados
packages = ['requests', 'pandas', 'matplotlib', 'os']

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Instala cada pacote usando o pip
for package in packages:
    print("\n")
    print( HEADER +'********************************'+ ENDC)
    print( BOLD + f'{package} instalando...' + ENDC)
    print( HEADER +'********************************'+ ENDC)
    print("\n")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

        print("\n")
        print( OKGREEN + '********************************' + ENDC)
        print( BOLD + f'{package} instalado com sucesso' + ENDC)
        print( OKGREEN + '********************************' + ENDC)
        print("\n")
    except:
        print( FAIL +'********************************' + ENDC)
        print( BOLD + f'Houve um erro no pacote: {package}' + ENDC)
        print( FAIL +'********************************' + ENDC)
        print("\n")
        print("\n")

