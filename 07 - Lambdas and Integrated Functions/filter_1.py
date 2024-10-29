# Serve para filtrar determinados dados de uma coleção

import statistics

print("----------------------------------------------------------------------------------------------------")

temperaturas = [23.4, 10.5, 15.6, 40.5, 33.9, 37.8, 1, -2, 41.5, 17.7]

media_temperaturas = sum(temperaturas) / len(temperaturas)

print(media_temperaturas)

print("----------------------------------------------------------------------------------------------------")

# Utilizando o filter

media_temperaturas = None

print(media_temperaturas)

print("----------------------------------------------------------------------------------------------------")

media_temperaturas = statistics.mean(temperaturas)

print(media_temperaturas) # Média das temperaturas = 21,99

print("----------------------------------------------------------------------------------------------------")

# Utilizando o filter para filtrar as temperaturas acima da média

altas_teperaturas = filter(lambda t: t > media_temperaturas, temperaturas) # Poderia ser calculado a média dentro da lambda (menos legível)

print(list(altas_teperaturas)) # [23.4, 40.5, 33.9, 37.8, 41.5]

print("----------------------------------------------------------------------------------------------------")

print(type(altas_teperaturas))

print("----------------------------------------------------------------------------------------------------")

print(f"Segunda consulta da lista {list(altas_teperaturas)}")

# OBS.: Assim como no map (AQUI O COMPORTAMENTO FOI O ESPERADO, AO CONTRÁRIO DO MAP), na segunda vez que consultamos a lista, ela aparece vazia.

print("----------------------------------------------------------------------------------------------------")
