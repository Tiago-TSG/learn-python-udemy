numeros = [1, 2, 3, 4, 5, 6]

print("----------------------------------------------------------------------------------------------------")

pares = [numero for numero in numeros if numero % 2 == 0 ]
impares = [numero for numero in numeros if numero % 2 != 0 ]

print(pares)
print(impares)

print("----------------------------------------------------------------------------------------------------")

# Outra forma

pares = [numero for numero in numeros if not numero % 2] # OBS.: Todo número zero é false em boleano "not False = True"

impares = [numero for numero in numeros if numero % 2] # OBS.: Qualquer número ímpar módulo de 2 = 1 é True em boleano.

print(pares)
print(impares)

print("----------------------------------------------------------------------------------------------------")

calculo = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

print(calculo)

print("----------------------------------------------------------------------------------------------------")
