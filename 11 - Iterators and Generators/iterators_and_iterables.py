"""
Iterator --> É um objeto que pode ser iterado. Ele retorna um dado (um elemento por vez), quando uma função next() é chamada.

Iterable --> Retorna um iterator, quando uma função iter() é chamada.

OBS: Um objeto pode ser iterável, mas não um iterator.
"""
print("----------------------------------------------------------------------------------------------------")

texto = "Hello, World!"  # string é iterável
numeros = [1, 2, 3, 4, 5]  # lista é iterável

# iterando sobre a string
iterador_texto = iter(texto)

print(next(iterador_texto))  # Output: 'H'
print(next(iterador_texto))  # Output: 'e'
print(next(iterador_texto))  # Output: 'l'

print("----------------------------------------------------------------------------------------------------")

# iterando sobre a lista
iterador_numeros = iter(numeros)

print(next(iterador_numeros))  # Output: 1
print(next(iterador_numeros))  # Output: 2
print(next(iterador_numeros))  # Output: 3
print(next(iterador_numeros))  # Output: 4
print(next(iterador_numeros))  # Output: 5

print("----------------------------------------------------------------------------------------------------")

"""
OBS: O for loop é um iterador de um objeto iterável.
"""
for letra in texto:
    print(letra)

print("----------------------------------------------------------------------------------------------------")
