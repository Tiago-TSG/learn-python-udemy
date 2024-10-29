"""
Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele possui.
"""

lista = []
count = 10

numeros_pares = 0

print("----------------------------------------------------------------------------------------------------")

while len(lista) < count:
    valor = int(input(f"Digite o número {len(lista) + 1}/{count}: "))
    lista.append(valor)

print("----------------------------------------------------------------------------------------------------")

for n in lista:
    if n % 2 == 0:
        numeros_pares = numeros_pares + 1

if numeros_pares > 0:
    print(f"A lista possui {numeros_pares} números pares.")
else:
    print(f"A lista não possui números pares.")

print("----------------------------------------------------------------------------------------------------")
