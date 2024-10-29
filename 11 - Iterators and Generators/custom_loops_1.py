# Laço de repetição FOR

# for item in sequência:
#   bloco de código a ser repetido

# Exemplo 1: Imprimindo números de 1 a 5

print("----------------------------------------------------------------------------------------------------")

for numero in range(1, 6):
    print(numero)

print("----------------------------------------------------------------------------------------------------")

# Exemplo 2: Imprimindo letras de uma string

nome = "Vasco da Gama"

for letra in nome:
    print(letra)

# Exemplo 3: Imprimindo números de 1 a 5 usando uma lista
# Obs: NÃO É UMA BOA PRÁTICA USAR UM LAÇO FOR COM UMA LISTA
# POIS O PYTHON FORNECE UMA FUNÇÃO PRONTA PARA ISSO
# range(1, 6) = [1, 2, 3, 4, 5]
# range(1, 11, 2) = [1, 3, 5, 7, 9]
# range(10, 0, -1) = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("----------------------------------------------------------------------------------------------------")

# Criando seu for customizado

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for(range(1, 11))

print("----------------------------------------------------------------------------------------------------")

meu_for("Vasco da Gama")

print("----------------------------------------------------------------------------------------------------")
