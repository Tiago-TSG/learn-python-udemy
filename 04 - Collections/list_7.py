print("----------------------------------------------------------------------------------------------------")

lista_1 = ["banana", "maçã", "pera", "uva", "limão", "melancia", "melão"]

lista_fruta = lista_1.copy()
print(lista_fruta)

print("----------------------------------------------------------------------------------------------------")

numeros = [0, 1, 2, 3]
print(numeros)

numeros_novos = numeros.copy() # Cria um novo ponteiro na memória.
print(numeros_novos)

numeros_novos.append(4)
print(numeros)
print(numeros_novos)

print("----------------------------------------------------------------------------------------------------")

numeros = [0, 1, 2, 3]
print(numeros)

numeros_novos = numeros # Aponta para o mesmo espaço de memória da outra variável (numeros)
print(numeros_novos)

numeros_novos.append(4)
print(numeros)
print(numeros_novos)


print("----------------------------------------------------------------------------------------------------")

print(len(lista_fruta))

lista_fruta.pop()
print(lista_fruta)

print("----------------------------------------------------------------------------------------------------")

lista_2 = ["jaca", "kiwi", "banana", "pêssego", "maçã", "pera", "uva","jabuticaba", "limão", "melancia", "melão", "abacate"] 
print(lista_2)

# OBS.: O método POP é acumulativo, alterando o valor contido nos índices a cada alteração.

lista_2.pop(-1)
print(lista_2)

lista_2.pop(1)
print(lista_2)

lista_2.pop(-2)
print(lista_2)

print("----------------------------------------------------------------------------------------------------")

lista_2.clear()
print(lista_2)

print("------------------------------------------------------------") 
