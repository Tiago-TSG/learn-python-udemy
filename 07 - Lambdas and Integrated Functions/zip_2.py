dados = ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5))

print("----------------------------------------------------------------------------------------------------")

print(list(zip(*dados))) # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

print("----------------------------------------------------------------------------------------------------")

alunos = ['Maria', 'João', 'Pedro']
prova_1 = [7.8, 8.9, 6.7]
prova_2 = [9.8, 6.5, 7.7]

print(set(zip(alunos, prova_1, prova_2))) # O que o zip retorna, convertido para um conjunto de tuplas.

print("----------------------------------------------------------------------------------------------------")

nota_final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova_1, prova_2)}

print(nota_final) # {'Maria': 9.8, 'João': 8.9, 'Pedro': 7.7}

print("----------------------------------------------------------------------------------------------------")

# Outra forma de obter o mesmo resultado, utilizando também o map()

nota_final = zip(alunos, map(lambda nota: max(nota), zip(prova_1, prova_2)))

print(dict(nota_final)) # {'Maria': 9.8, 'João': 8.9, 'Pedro': 7.7}

print("----------------------------------------------------------------------------------------------------")

# Outro exemplo, calculando a média das notas

nota_final = {dado[0]: (dado[1] + dado[2])/2 for dado in zip(alunos, prova_1, prova_2)}

print(nota_final) # {'Maria': 8.8, 'João': 7.7, 'Pedro': 7.2}

print("----------------------------------------------------------------------------------------------------")

# Outra forma de obter o mesmo resultado, utilizando também o map()

nota_final = zip(alunos, map(lambda nota: (nota[0] + nota[1])/2, zip(prova_1, prova_2)))

print(dict(nota_final)) # {'Maria': 8.8, 'João': 7.7, 'Pedro': 7.2}

print("----------------------------------------------------------------------------------------------------")
