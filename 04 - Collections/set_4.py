dados = 66, 54, 33, 88, 24, 67, 2, 34, 78, 99, 13, 2, 33

lista = list(dados)

tupla =  tuple(dados)

dicionario = {}.fromkeys(dados, "")

conjunto = set(dados)


print("----------------------------------------------------------------------------------------------------")

print(f" A lista tem {len(lista)} elementos.")

print("----------------------------------------------------------------------------------------------------")

print((f" A tupla tem {len(tupla)} elementos."))

print("----------------------------------------------------------------------------------------------------")

print(f" O dicionário tem {len(dicionario)} elementos.")

print("----------------------------------------------------------------------------------------------------")

print(f" O conjunto tem {len(conjunto)} elementos.")

print("----------------------------------------------------------------------------------------------------")
