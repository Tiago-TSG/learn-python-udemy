# O reversed() é diferente do reverse() que só pode ser utilizado em listas.
# O reversed() pode ser utilizado em qualquer tipo de iterável.
# Ele retorna um objeto do tipo list_reverseiterator que pode ser convertido para uma lista comum, tupla ou conjunto

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("----------------------------------------------------------------------------------------------------")

reversed_list = reversed(lista)

print(reversed_list)
print(type(reversed_list))

print("----------------------------------------------------------------------------------------------------")

print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista))) # OBS.: Em conjuntos, não são definidas a ordem dos elementos.

print("----------------------------------------------------------------------------------------------------")

for letra in reversed('Vasco da Gama'):
    print(letra, end=' ')

print('\n')

print("----------------------------------------------------------------------------------------------------")

# Fazendo o mesmo sem o uso do loop FOR

print((list(reversed('Vasco da Gama')))) # Com o "list", transformamos a string em uma lista de strings.

print("----------------------------------------------------------------------------------------------------")

print(' '.join(list(reversed('Vasco da Gama')))) # Quando adicionarmos o ' '.join, convertemos a lista para um string novamente.

# Outra forma ainda mais fácil seria utilizando slicing

print(' '.join("Vasco da Gama"[::-1]))

print("----------------------------------------------------------------------------------------------------")

# Também podemos utilizar o reversed dentro de um loop FOR

for n in reversed(lista):
    print(n)

print("----------------------------------------------------------------------------------------------------")

for n in reversed(range(1, 11)):
    print(n)

print("----------------------------------------------------------------------------------------------------")

# Fazendo o mesmo, sem utilizar o reversed

for n in range(10, 0, -1):
    print(n)

print("----------------------------------------------------------------------------------------------------")
