lista = [1, 6, 10, 33, 24, 46, 13, 56, 89, 5, 99, 18, 17, 21]

count_par = 0
count_impar = 0

for n in lista:
    if n % 2 == 0:
        count_par = count_par + 1
    else:
        count_impar = count_impar + 1

print(f"A lista possui {count_par} números pares e {count_impar} números ímpares.")

print(f"O número total de números na lista é {len(lista)}.")
