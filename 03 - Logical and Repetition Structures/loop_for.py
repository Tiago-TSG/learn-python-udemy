seq_num=int(input("Informe um número para uma sequência de somas: "))

soma = 0

for n in range(1, seq_num + 1):
    num = int(input(f"Escolha o valor do número {n}/{seq_num}: "))
    soma = soma + num
print(f"A soma total dos números é {soma}.")
