# Generator é um tuple comprehension.
# É mais performático que uma list comprehension, set comprehension ou o dict comprehension, pois ocupa menos espaço na memória.


print("----------------------------------------------------------------------------------------------------")

nomes = ["Julia", "Juliana", "Juliete", "Jurema", "Jupira", "Evelyn"]

print(any(nome[0] == "E" for nome in nomes)) # O generator é processado diretamente sem ocupar espaço na memória.

print("----------------------------------------------------------------------------------------------------")

resultado = (nome[0] == "E" for nome in nomes)

print(type(resultado))
print(resultado)

print("----------------------------------------------------------------------------------------------------")

resultado = [nome[0] == "E" for nome in nomes]

print(type(resultado))
print(resultado)

print("----------------------------------------------------------------------------------------------------")

# Utilizando a biblioteca do getsizeof para obter o tamanho em memória (bytes) ocupado por dados no Python

from sys import getsizeof

print(getsizeof(nomes)) # 104
print(getsizeof("Vasco")) # 54
print(getsizeof([7])) # 64
print(getsizeof(range(1, 11))) # 48
print(getsizeof([])) # 56
print(getsizeof(())) # 40
print(getsizeof({})) # 64
print(getsizeof(True)) # 28

print("----------------------------------------------------------------------------------------------------")
