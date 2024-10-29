from math import sqrt

num = int(input("Digite um número inteiro: "))

if num > 0:
    #print(f"A raiz quadrada de {num} é {num ** (1/2)}.") --> Também funciona
    print(f"A raiz quadrada de {num} é {sqrt(num)}.")
else:
    print(f"Número {num} inválido.")
    