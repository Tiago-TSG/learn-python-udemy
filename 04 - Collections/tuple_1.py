print("----------------------------------------------------------------------------------------------------")

tuple_1 = (1, 2, 3, 4) # É uma tupla
print(tuple_1)
tuple_2 = 1, 2, 3, 4 # É uma tupla
print(tuple_2)
tuple_3 = (4) # Não é uma tupla (Não tem vírgula)
print(tuple_3)
tuple_4 = 1, 5 # É uma tupla
print(tuple_4)
tuple_5 = (1, ) # É uma tupla
print(tuple_5)
tuple_6 = 5, # É uma tupla

print("----------------------------------------------------------------------------------------------------")

tuple = tuple(range(11))
print(tuple)

print("----------------------------------------------------------------------------------------------------")

tuple_endereco = ("Estrada Adhemar Bebiano", "257", "Bloco", "3", "Apartamento", "808", "Del Castilho", "Rio de Janeiro")

logradouro, numero, bloco_casa, numero_bloco_casa, tipo_apt_casa, número_apt_casa, bairro, estado = tuple_endereco

print(tuple_endereco)
print(" - ".join(tuple_endereco))

print("----------------------------------------------------------------------------------------------------")

tuple_endereco_resumido = logradouro, numero

print(tuple_endereco_resumido)
print(" - ".join(tuple_endereco_resumido))

print("----------------------------------------------------------------------------------------------------")
