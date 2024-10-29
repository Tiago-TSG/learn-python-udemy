print("----------------------------------------------------------------------------------------------------")

def mostra_nomes(**kwargs):
    return(f"{kwargs['nome']} {kwargs['sobrenome']}")

nomes = {"nome": "Tiago", "sobrenome": "Gonçalves"}

print(mostra_nomes(**nomes)) # OBS.: Maneira de desempacotar um dicionário

print("----------------------------------------------------------------------------------------------------")

def soma_numeros(a, b, c):
    print(a + b + c)

lista = [2, 4, 6]
tupla = (2, 4, 6)
conjunto = {2, 4, 6}

soma_numeros(*lista) # OBS.: Para o desempacotamento de listas (args), se utiliza asterístico simples (*).
soma_numeros(*tupla) # OBS.: Para o desempacotamento de tuplas (args), se utiliza asterístico simples (*).
soma_numeros(*conjunto) # OBS.: Para o desempacotamento de conjuntos (args), se utiliza asterístico simples (*).

print("----------------------------------------------------------------------------------------------------")

dicionario = dict(a=2, b=4, c=6) # OBS.: Para dicionário, as chaves tem que ser igual aos parâmetros declarados na função.

soma_numeros(**dicionario) # OBS.: Para o desempacotamento de um dicionário (kwargs), se utiliza duplo asterístico (**).

print("----------------------------------------------------------------------------------------------------")

def soma_numeros_nova(a, b, c, **kwargs):
    print(f"{a + b + c} --> {kwargs}")

dicionario_novo = dict(a=1, b=3, c=6, time = "Vasco")
dicionario_novo_2 = dict(a=1, b=3, c=6, time1 = "Vasco", time2 = "Fluminense")

soma_numeros_nova(**dicionario_novo)
soma_numeros_nova(**dicionario_novo_2)

print("----------------------------------------------------------------------------------------------------")
