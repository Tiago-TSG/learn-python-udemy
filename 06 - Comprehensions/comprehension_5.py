chaves = "abcdefghil"

valor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mistura = {chaves[i]: valor[i] for i in range(0, len(chaves))} # Iterando em uma string e uma lista

print("----------------------------------------------------------------------------------------------------")

print(mistura)

print("----------------------------------------------------------------------------------------------------")

numeros = [2, 3, 6, 7, 9, 1, 44, 5, 33, 68, 79]

par_ou_impar = {n: ("Par" if n % 2 == 0 else "Impar") for n in numeros}

print(par_ou_impar)

print("----------------------------------------------------------------------------------------------------")

numeros = {num for num in range(1,11)}

print(numeros)

print("----------------------------------------------------------------------------------------------------")

numeros = {num ** 2 for num in range(1,11)}

print(numeros)

print("----------------------------------------------------------------------------------------------------")

numeros_e_quadrados = {num: (num ** 2) for num in range(1,11)}

print(numeros_e_quadrados)

print("----------------------------------------------------------------------------------------------------")

letras = {letras for letras in "Vasco da Gama"} # OBS: Conjuntos não mantém ordenação e não repetem itens

print(letras)

print("----------------------------------------------------------------------------------------------------")
