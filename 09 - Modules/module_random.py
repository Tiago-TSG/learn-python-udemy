# O módulo random possui várias funções embutidas.
# O ideal é importar somente as funções que forem utilizadas, para não sobrecarregar a memória.

# OBS.: É possíve também definir um apelindo para o módulo, utilizando o "as".
# Exemplo: import random as rdm (Obs.: na hora de chamar o o módulo, será necessário informar o apelido no lugar do nome).

# Também é possível importar todas as funções de uma função, utilizando o "*".  Exemplo: from random import *

# OBS.: "from random import *"  é diferente de "import random" . Ambos importam o módulo todo, mas somente da primeira forma, 
# não é preciso informar o módulo quando se chama a função (ex: print(random()) ao invés de print(random.random()))

# Também é possível utilizar apelidos para módulos/funções.
# exemplo-1: "from random import randint as rdi"
# exemplo-2: "from random import randint as rdi, shuffle as shfe"

from random import random, uniform, randint, choice, shuffle

# OBS.: Uma outra forma de importar múltiplas funções de forma mais legível (dependendo do número de funções) é através de uma tupla.
# Exemplo:
#
# from random import(
#    random,
#    uniform,
#    randint,
#    choice,
#    shuffle
# )

# A função random, gera números pseudo-randômicos entre "0" e "1".

print("----------------------------------------------------------------------------------------------------")

for i in range(10):
    print(random())

print("----------------------------------------------------------------------------------------------------")

# A função uniform, gera números pseudo-randômicos dentro de um intervalo especificado.

for i in range(10):
    print(uniform(3, 7)) # O "7" é excluído das possíveis saídas.

print("----------------------------------------------------------------------------------------------------")

# A função uniform, gera números inteiros pseudo-randômicos dentro de um intervalo especificado.
# Exemplo de código que poderia ser utilizado em uma loteria, por exemplo:

for i in range(6):
    print(randint(1,61)) # OBS.: Pode ser que venham números repetidos.
    
print("----------------------------------------------------------------------------------------------------")

# A função choice, exibe uma valor aleatório entre elementos de um iterável.

jogadas = ["pedra", "papel", "tesoura"]

print(choice(jogadas))

print("----------------------------------------------------------------------------------------------------")

print(choice("Vasco da Gama")) # Imprime uma letra aleatória dentre as possíveis na string passada.

print("----------------------------------------------------------------------------------------------------")

# A função shuffle, embaralha valores de um iterável.

cartas = ['Q', 'J', 'K', 'A', '2', '3', '4', '5', '6', '7', '8']

print(cartas)
shuffle(cartas)
print(cartas)

print(cartas[0])
print(cartas.pop())

print("----------------------------------------------------------------------------------------------------")
