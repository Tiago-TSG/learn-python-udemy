# O "zip" cria um iterável Zip object que agrega os elementos de cada um dos iteráveis informados.

lista_1 = ['a', 'b', 'c', 'd', 'e']
lista_2 = [1, 2, 3, 4, 5]
lista_3 = [6, 7, 8]
lista_4 = ['f', 'g', 'h', 'i', 'j']
dicionário = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

print("----------------------------------------------------------------------------------------------------")

lista_final = zip(lista_1, lista_2)

print(lista_final) # Não imprime nada
print(type(lista_final)) # Tipo "class zip"

print("----------------------------------------------------------------------------------------------------")

# OBS.: O zip só permite imprimir uma vez o resultado (tira da memória). 
# Por isso é necessário repetir a variável "lista_final" para cada impressão na tela.

print(list(lista_final)) # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

lista_final = zip(lista_1, lista_2) 
print(tuple(lista_final)) # (('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5))

lista_final = zip(lista_1, lista_2) 
print(set(lista_final)) # {('b', 2), ('a', 1), ('d', 4), ('e', 5), ('c', 3)}
 
lista_final = zip(lista_1, lista_2) 
print(dict(lista_final)) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

print("----------------------------------------------------------------------------------------------------")

lista_final = zip(lista_1, lista_2, lista_3) # OBS.: O zip limita o seu zip object pelo iterável com menor número de elementos.
print(list(lista_final)) # [('a', 1, 6), ('b', 2, 7), ('c', 3, 8)]

print("----------------------------------------------------------------------------------------------------")

lista_final = zip(lista_1, lista_2, lista_4)
print(list(lista_final)) # [('a', 1, 'f'), ('b', 2, 'g'), ('c', 3, 'h'), ('d', 4, 'i'), ('e', 5, 'j')]

print("----------------------------------------------------------------------------------------------------")

lista_final = zip(lista_1, lista_2, 'vasco') # [('a', 1, 'v'), ('b', 2, 'a'), ('c', 3, 's'), ('d', 4, 'c'), ('e', 5, 'o')]
print(list(lista_final))

print("----------------------------------------------------------------------------------------------------")

lista_final = zip(lista_1, lista_2, ['vasco']) # [('a', 1, 'vasco')]
print(list(lista_final))

print("----------------------------------------------------------------------------------------------------")

lista_final = zip(dicionário.keys(), lista_2) # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
print(list(lista_final))

lista_final = zip(lista_1, dicionário.values()) # [('a', 11), ('b', 12), ('c', 13), ('d', 14), ('e', 15)]
print(list(lista_final))

print("----------------------------------------------------------------------------------------------------")
