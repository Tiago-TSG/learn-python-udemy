lista_1 = ["jaca", "kiwi", "banana", "pêssego", "maçã"]

print("----------------------------------------------------------------------------------------------------")

lista_2 = lista_1 * 3
print(lista_2)

lista_3 = lista_1.extend(lista_1)
print(lista_1)

print("----------------------------------------------------------------------------------------------------")

time = "Vasco da Gama"
print(time)

time = time.split() # Por padrão o split separa os elementos da lista pelo espaço contido entre as palavras.
print(time)

print("----------------------------------------------------------------------------------------------------")

endereco = "Estrada Adhemar Bebiano, 257 - Bloco 3, Apartamento 808 - Del Castilho - Rio de Janeiro"
print(endereco)

endereco = endereco.split("-") # Fazendo a separação da lista pelo "-" contido entre os elementos contidos nela.
print(endereco)

print("----------------------------------------------------------------------------------------------------")

lista_endereco = ['Estrada Adhemar Bebiano, 257 ', ' Bloco 3, Apartamento 808 ', ' Del Castilho ', ' Rio de Janeiro']
print (lista_endereco)

string_endereco = "-".join(lista_endereco) # Fazendo junção da string pelo "-" contido entre os elementos.
print(string_endereco)

print("----------------------------------------------------------------------------------------------------")
