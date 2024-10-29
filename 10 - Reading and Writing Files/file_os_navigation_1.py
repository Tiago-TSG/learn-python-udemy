# Para trabalhar com diretórios e paths do diferentes do sistema operacional, podemos usar o módulo OS.

print("----------------------------------------------------------------------------------------------------")

import os

# getcwd() --> Função que obtém o caminho absoluto atual.

print(os.getcwd())

# chdir() --> Função que muda o diretório corrente.

os.chdir('..')

print(os.getcwd())

os.chdir('..')

print(os.getcwd())

os.chdir('..')

print(os.getcwd())

print("----------------------------------------------------------------------------------------------------")

# path.join --> Função usada para unir paths.

os.chdir('/home/tiago/estudos/python/geek-university')

print(os.getcwd())

res = os.path.join(os.getcwd(), 'package_1')

os.chdir(res)

print(os.getcwd())

print("----------------------------------------------------------------------------------------------------")
