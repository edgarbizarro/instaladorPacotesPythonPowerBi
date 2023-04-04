import subprocess
import sys

# Lista de pacotes a serem instalados
packages = ['requests', 'pandas', 'matplotlib', 'os']

# Instala cada pacote usando o pip
for package in packages:
    print(package)
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
