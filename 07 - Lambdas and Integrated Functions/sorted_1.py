# O sorted() é diferente do sort().
# O "sort()"" é uma função que só serve para listas, enquanto o "sorted()" pode ser utilizado em qualquer tipo de coleção.
# O sort() altera a lista, enquanto o sorted() gera uma nova lista (obs.: sempre retorna uma lista) e não altera a original.

print("----------------------------------------------------------------------------------------------------")

numeros = [9, 2, 10, 7, 5, 1, 8, 6, 4, 3]

print(numeros.sort()) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numeros) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("----------------------------------------------------------------------------------------------------")

numeros = [9, 2, 10, 7, 5, 1, 8, 6, 4, 3]

print(sorted(numeros)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sorted(numeros, reverse = True)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] --> Ordeand

print(numeros) # [9, 2, 10, 7, 5, 1, 8, 6, 4, 3]  --> OBS.: Com o sorted() a lista original é mantida.

print("----------------------------------------------------------------------------------------------------")


print(numeros) # [9, 2, 10, 7, 5, 1, 8, 6, 4, 3] --> Obs.: Manutenção da lista original

print(tuple(sorted(numeros))) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) --> Tranformando a lista em uma tupla ordenada.

print(set(sorted(numeros))) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} -->  Tranformando a lista em um conjunto ordenado.

print("----------------------------------------------------------------------------------------------------")
