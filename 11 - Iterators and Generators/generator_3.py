# Generators (Geradores)

def nums():
    for num in range(1, 11):
        yield num

gen1 = nums()

print("----------------------------------------------------------------------------------------------------")

print(gen1) # Generator object

print("----------------------------------------------------------------------------------------------------")

print(next(gen1)) # 1
print(next(gen1)) # 2

print("----------------------------------------------------------------------------------------------------")

# Generator Expression

gen2 = (num for num in range(1, 11))

print(gen2) # Generator object

print("----------------------------------------------------------------------------------------------------")

print(next(gen2)) # 1
print(next(gen2)) # 2

print("----------------------------------------------------------------------------------------------------")

# Realizando teste de perfomance

from time import time

# Generator Expression

gen_inicio = time()
print(sum(num for num in range(100000000))) # 100 milhões
gen_tempo = time() - gen_inicio

print("----------------------------------------------------------------------------------------------------")

# List Comprehension

list_inicio = time()
print(sum([num for num in range(100000000)])) # 100 milhões
list_tempo = time() - list_inicio

print("----------------------------------------------------------------------------------------------------")

print(f" O Generator Expression levou: {gen_tempo} segundos.")
print(f" O List Comprehension levou: {list_tempo} segundos.")

print("----------------------------------------------------------------------------------------------------")
