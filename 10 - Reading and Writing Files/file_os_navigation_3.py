import os

print("----------------------------------------------------------------------------------------------------")

# path.isabs() --> Função para checar se um path é absoluto. Retorna "True" ou "False"

print(os.path.isabs('/home/tiago/estudos/python/geek-university'))
print(os.path.isabs('/home/tiago/estudos/python'))

print(os.path.isabs('estudos/python/geek-university'))
print(os.path.isabs('estudos/python'))

print(os.path.isabs('../../python/geek-university'))
print(os.path.isabs('../geek-university'))

print(os.path.isabs('../geek-university'))

print("----------------------------------------------------------------------------------------------------")

# name --> Identifica o sistema operacional vigente (posix --> Linux e Mac, nt --> Windows)
# uname() --> Apresenta maiores detalhes sobre o sistema operacional

print(os.name)
print(os.uname())

print("----------------------------------------------------------------------------------------------------")

# Outro módulo para obter outros tipos de informações do sistema

import sys 

print(sys.platform)

print("----------------------------------------------------------------------------------------------------")
