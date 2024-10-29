# Para instalar módulos que não são padrão do Python (módulos externos), utilizamos o PIP (Python Installer Package)
# Para conhecer diversos módulos externos, basta acessar o site https://pypi.org

# Para instalar o módulo, basta utilizar o comando "pip install "nome do módulo"

# Para instalar o módulo externo colorama, basta utilizar o comando "pip install colorama" .

from colorama import init, Fore

print(Fore.RED + "Vasco da Gama")
print(Fore.BLACK + "Vasco da Gama")


# Para instalar o módulo externo "pydf", basta utilizar o comando "pip install python-pdf" .

import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1><br/><br/><strong>Programa&ccedil;&atilde;o em Python: Essencial<strong/>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
