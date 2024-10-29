print("----------------------------------------------------------------------------------------------------")

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5, 'g': 6}

print(numeros.items())

print("----------------------------------------------------------------------------------------------------")

quadrados = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrados)

print("----------------------------------------------------------------------------------------------------")


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Iterando em uma lista

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)


numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # Iterando em uma tupla

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)


numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} # Iterando em um conjunto

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)

print("----------------------------------------------------------------------------------------------------")
