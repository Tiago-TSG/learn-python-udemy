
print("----------------------------------------------------------------------------------------------------")

novo_dicionario = {}.fromkeys("a","b") # O método fromkeys funciona com dois parâmetros (um iterável e um valor)
print(novo_dicionario)
print(type(novo_dicionario))

print("----------------------------------------------------------------------------------------------------")

paises_siglas = {}.fromkeys(["Brasil", "Argentina", "Estados Unidos", "Japão"], "")
print(paises_siglas)

print("----------------------------------------------------------------------------------------------------")

time = {}.fromkeys(["time"], ["Vasco da Gama"])
print(time)
print(time["time"])

time = {}.fromkeys("time", "Vasco da Gama")
print(time)


dicionario_range = {}.fromkeys(range(1,11), "novo")
print(dicionario_range)


print("----------------------------------------------------------------------------------------------------")
