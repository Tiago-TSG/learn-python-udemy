""" 
Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores lidos.

"""

lista = []
count = 6

print("----------------------------------------------------------------------------------------------------")

while len(lista) < count:
    valor = int(input(f"Digite um número inteiro {len(lista) + 1}/{count}: "))
    lista.append(valor)

print("----------------------------------------------------------------------------------------------------")

for valor in lista:
    print(valor)

print("----------------------------------------------------------------------------------------------------")

print(f"lista = {lista}")

print("----------------------------------------------------------------------------------------------------")
