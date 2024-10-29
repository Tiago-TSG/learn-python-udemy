# O map (Obs.:diferente do mapa que é o equivalente ao dicionário) faz o mapeamento de valores para uma função.

# Função = f(x)
# map(f, dados)

import math

print("----------------------------------------------------------------------------------------------------")

def area(r):
    return(math.pi * (r ** 2))

print(area(2))
print(area(4))

print("----------------------------------------------------------------------------------------------------")

# Forma comum

raios = [2, 4, 6, 8, 10]

areas = []

for r in raios:
    areas.append((area(r)))

print(areas)

print("----------------------------------------------------------------------------------------------------")

# Forma - 2 (O map é uma função que recebe dois parâmetros. O primeiro é uma função e o segundo é um iterável.)

areas = map(area, raios)

print(list(areas))

print("----------------------------------------------------------------------------------------------------")

print(type(areas))

print("----------------------------------------------------------------------------------------------------")

# Forma - 3 (map com lambda)

print(list(map(lambda r: math.pi * ( r ** 2), raios)))

# OBS.: Após utilizar a função map uma vez, o python limpa a memória ( NOS TESTES QUE EU FIZ COM ESSA VERSÃO DO PYTHON, ISSO NÃO OCORREU )

print("----------------------------------------------------------------------------------------------------")

# Outro exemplo:

cidades_temperatura = [("Berlim", 29), ("Ciro", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Berlim", 29), ("Rio de Janeiro", 40), ("Tokio", 27)]

print(cidades_temperatura)

print("----------------------------------------------------------------------------------------------------")

# Conversão de Celsius para "Fahrenheit" --> f = (c * 9/5) + 32

c_para_f = lambda dado: (dado[0], (dado[1] * 9/5) + 32)

print(list(map(c_para_f, cidades_temperatura)))

print("----------------------------------------------------------------------------------------------------")
