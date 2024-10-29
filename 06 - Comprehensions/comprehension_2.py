numeros = [1, 2, 3, 4, 5]

print("----------------------------------------------------------------------------------------------------")

# Utilizando Loop com "for"

numeros_dobro = []

for n in numeros:
    numeros_dobro.append(n * 2)

print(numeros_dobro) # [2, 4, 6, 8, 10]

# Utilizando o List Comprehension

print([n * 2 for n in numeros]) # [2, 4, 6, 8, 10]

print("----------------------------------------------------------------------------------------------------")

time = "vasco da gama"

print([letra.upper() for letra in time]) # ['V', 'A', 'S', 'C', 'O', ' ', 'D', 'A', ' ', 'G', 'A', 'M', 'A']

print("----------------------------------------------------------------------------------------------------")

amigos = ["tiago", "william", "edson", "david"]

print([amigo.capitalize() for amigo in amigos]) # ['Tiago', 'William', 'Edson', 'David']

print("----------------------------------------------------------------------------------------------------")

print([n * 3 for n in range(1, 11)]) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

print("----------------------------------------------------------------------------------------------------")

print([bool(valor) for valor in [0, "", True, [], 2, 3.43]]) # [False, False, True, False, True, True]

print("----------------------------------------------------------------------------------------------------")

print([str(numero) for numero in numeros])

print("----------------------------------------------------------------------------------------------------")
