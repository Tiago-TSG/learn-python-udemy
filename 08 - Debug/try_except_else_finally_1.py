# Toda entrada de dados deve ser tratada.

print("----------------------------------------------------------------------------------------------------")

num_1 = 0 # Não é o melhor formato de se tratar esse tipo de problema.

try:
    num_1 = int(input("Digite um número: "))
except ValueError:
    print("Você digitou um valor incorreto.")

print(f"Você digitou o número {num_1}.")

print("----------------------------------------------------------------------------------------------------")

# Formato melhor de se tratar esse tipo de problema.

try:
    num_2 = int(input("Digite um número: "))

except ValueError:
    print("Você digitou um valor incorreto.")

else:
    print(f"Você digitou o número {num_2}.") # Se não ocorrer o erro, esse print é executado.

print("----------------------------------------------------------------------------------------------------")

# Utilizando o finally (É sempre executado independente se houver excessão ou não.)

try:
    num_3 = int(input("Digite um número: "))

except ValueError:
    print("Você digitou um valor incorreto.")

else:
    print(f"Você digitou o número {num_3}.") # Se não ocorrer o erro, esse print é executado.

finally:
    print(f"Excutando o finally.") # OBS.: O finally desacola recursos, finalizando seções com bancos de dados e fechando arquivos.

print("----------------------------------------------------------------------------------------------------")
