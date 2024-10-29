# O "all" retorna "True", se todos os elementos forem verdadeiros (Obs.: O "0" é tratado como False, e vazio "" como True)

print("----------------------------------------------------------------------------------------------------")

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(all(numeros)) # False

print("----------------------------------------------------------------------------------------------------")

lista = []

print(all(lista)) # True

print("----------------------------------------------------------------------------------------------------")

pares = [n for n in numeros if n % 2 == 0]

print(pares) # [0, 2, 4, 6, 8]
print(all(pares)) # False

print("----------------------------------------------------------------------------------------------------")

impares = [n for n in numeros if n % 2 != 0]

print(impares) # [1, 3, 5, 7, 9]
print(all(impares)) # True

print("----------------------------------------------------------------------------------------------------")

nomes = ["Julia", "Juliana", "Juliete", "Jurema", "Jupira", "Evelyn"]

print(all(nome[0] == "J" for nome in nomes))

print("----------------------------------------------------------------------------------------------------")

print(all("Vasco da Gama")) # True

print("----------------------------------------------------------------------------------------------------")

# O "any" retorna "True" se qualquer elemento de uma coleção for verdadeiro (Obs.: Ao contrário do all, o any retorna false para"vazio" )

print(any(numeros)) # True

print(any(lista)) # False

print("----------------------------------------------------------------------------------------------------")

print(any(pares)) # True

print(any(impares)) # True

print("----------------------------------------------------------------------------------------------------")

print(any([0, False, [], ()])) # False

print("----------------------------------------------------------------------------------------------------")

print(any(nome[0] == "E" for nome in nomes)) # True

print("----------------------------------------------------------------------------------------------------")
