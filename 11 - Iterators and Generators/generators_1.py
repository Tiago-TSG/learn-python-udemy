# Generators são iterators
# Nem todo iterator é um generator

# Generators podem ser criados com funções geradoras
# Funções geradoras (generators functions) utilizam a palavra reservada "yield".
# Generators podem ser criados com expressões geradoras.


"""
Diferenças entre funções e funções geradoras (generator functions):
"""

# ------------------------------------------------------------------------------------------#
# Funções                                 | Generator Functions                             #
# ------------------------------------------------------------------------------------------#
# Utilizam return                         | Utilizam yield                                  #
# ------------------------------------------------------------------------------------------#
# Retorna somente uma vez                 | Podem utilizar yield múltiplas vezes            #
# ------------------------------------------------------------------------------------------#
# Quando executada, retorna um valor      | Quando executada, retorna um generator          #
# ------------------------------------------------------------------------------------------#

"""
Exemplo de função geradora (generator function)
"""

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador # O yield é equivalente ao return, porém não sai da função, somente permanece no mesmo lugar esperando um "next()".
        contador += 1

# OBS: A Função geradora só é encerrada após a iteração em todos os elementos.

print("----------------------------------------------------------------------------------------------------")

gen = conta_ate(5)

print(gen) # <generator object conta_ate at 0x7f221c3ef6d0>
print(type(gen)) # <class 'generator'

print("----------------------------------------------------------------------------------------------------")

print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
print(next(gen)) # 4
print(next(gen)) # 5

# print(next(gen)) # StopIteration

print("----------------------------------------------------------------------------------------------------")

gen = conta_ate(10)

print(next(gen)) # Obs.: Como estou usando o next() aqui, o "for" iniciará do próximo número (2).

print("----------------------------------------------------------------------------------------------------")

for num in gen:  # Iterando no gen, podemos imprimir todos os valores contidos no generator.
    print(num)

print("----------------------------------------------------------------------------------------------------")

gen = list(conta_ate(20)) # Com o list, todos os elementos da função geradora são armazenados nela e ela é encerrada.

print(gen)

print("----------------------------------------------------------------------------------------------------")
