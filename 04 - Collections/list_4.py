num = int(input("Escolha um número de 1 até 100: "))

lista = [1, 6, 10, 33, 24, 46, 13, 56, 89, 5, 99, 18]

if num in lista:
    print(f"O número {num} está na lista.")
else:
    print(f"O número {num} não está na lista.")
