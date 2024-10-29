print("----------------------------------------------------------------------------------------------------")

from sys import getsizeof

list_size = getsizeof([x * 10 for x in range(1000)])

set_size = getsizeof({x * 10 for x in range(1000)})

dict_size = getsizeof({x: x * 10 for x in range(1000)})

generator_size = getsizeof(x * 10 for x in range(1000))


print(f"{list_size} bytes") # 9016 bytes (OBS.: Uma lista é a segunda coleção que ocupa menos espaço em memória devido a sua baixa complexidade.)

print(f"{set_size} bytes") # 32984 bytes

print(f"{dict_size} bytes") # 36960 bytes

print("----------------------------------------------------------------------------------------------------")

print(f"{generator_size} bytes") # 112 bytes (OBS.: O generator ocupa menos espaço que os comprehensions (list, set e dict))

print("----------------------------------------------------------------------------------------------------")

gen = (x * 10 for x in range(1000))
print(type(gen))
print(gen)

print("----------------------------------------------------------------------------------------------------")

for num in gen:
    print(f'{num}', end=" ") # É possível iterar com um generator desta maneira.

print("\n")
print("----------------------------------------------------------------------------------------------------")
