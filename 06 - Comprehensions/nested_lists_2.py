listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3x3

print("----------------------------------------------------------------------------------------------------")

# Utilizando o Comprehension

[[print(valor) for valor in lista] for lista in listas]

print("----------------------------------------------------------------------------------------------------")

tabuleiro = [[numero for numero in range(1,4)] for valor in range(1,4)]

print(tabuleiro)

print("----------------------------------------------------------------------------------------------------")

velha = [["X" if numero % 2 == 0 else "O" for numero in range(1,4)] for valor in range(1,4)]

print(velha)

print("----------------------------------------------------------------------------------------------------")

# Gerando valores iniciais

print([["*" for i in range(1,4)] for j in range(1,4)])

print("----------------------------------------------------------------------------------------------------")
