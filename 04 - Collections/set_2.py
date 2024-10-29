dados = 1, 2, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 10

print("----------------------------------------------------------------------------------------------------")

print(list(dados)) # Lista
print(len(list(dados)))

print(tuple(dados)) # Tupla
print(len(tuple(dados)))

print({}.fromkeys(list(dados), "dict")) # Dicionário
print(len({}.fromkeys(list(dados), "dict"))) # Dicionário

print(set(dados)) # Conjunto
print(len(set(dados)))

print("----------------------------------------------------------------------------------------------------")

conjunto = set(dados)
print(conjunto)

print("----------------------------------------------------------------------------------------------------")

for valor in conjunto:
    print(valor)

print("----------------------------------------------------------------------------------------------------")
