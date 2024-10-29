lista = [1, 6, 10, 33, 24, 46, 13, 56, 89, 5, 99, 18, 17, 21]

print("------------------------------------------------------------") 

lista.sort() # ordena os itens de uma lista.
print(lista)

print("------------------------------------------------------------") 

print(lista)
lista.append(11) # Permite somente 1 elemento por vez.
print(lista)

lista.extend([77, 41, 3]) # Permite adicionar múltiplos elementos em uma lista.
print(lista)

lista.append([4, 22]) # Adiciona uma sub lista dentro da lista já existente.
print(lista)

lista.extend(["Vasco da Gama"]) # Permite adicionar múltiplos elementos em uma lista.
print(lista)

lista.extend("Vasco da Gama") # Permite adicionar múltiplos elementos em uma lista.
print(lista)

lista.insert(0, "Novo Valor")
print(lista)

print("------------------------------------------------------------") 

lista_2 = ["a","b","c","d"]
lista_3 = ["e","f","g","h"]

lista_4 = lista_2 + lista_3
print(lista_4)

# --------- ou -------------- 

lista_2.extend(lista_3)
print(lista_2)

print("------------------------------------------------------------")
