print("----------------------------------------------------------------------------------------------------")

print(len('Vasco da Gama')) # 13

print("----------------------------------------------------------------------------------------------------")

print(len([1, 2, 3, 4, 5])) # 5
print(len((1, 2, 3, 4, 5))) # 5
print(len({1, 2, 3, 4, 5})) # 5

print(len({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})) # 5
print(len(dict(a=1, b=2, c=3, d= 4, e= 5))) # 5

print("----------------------------------------------------------------------------------------------------")

print(len(range(1, 11))) # 10

# Por debaixo dos panos, quando utilizamos a função "len" o Python utiliza " .__leb__() " (DUNDER LEN) .

print((range(1, 11)).__len__()) # 10

print("----------------------------------------------------------------------------------------------------")

# O "abs" retorna o valor absoluto de um número inteiro ou real.

print(abs(-5)) # 5
print(abs(5)) # 5

print(abs(-3.14)) # 3.14
print(abs(3.14)) # 3.14

print("----------------------------------------------------------------------------------------------------")

# O "sum" recebe um iterável, podendo retornar um valor inicial e retorna a soma dos elementos.

print(sum([1, 2, 3, 4, 5])) # 15
print(sum((1, 2, 3, 4, 5))) # 15
print(sum({1, 2, 3, 4, 5})) # 15
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values())) # OBS.: Necessário passar o " .values() " para retornar a soma dos valores e não das strings. # 15

print("----------------------------------------------------------------------------------------------------")

# O "round" retorna um número arredondado para n digitos de precisão após a casa decimal. Se a precisão não for informada, retorna o número inteiro mais próximo.

print(round(10.2)) # 10
print(round(10.5)) # 10 
print(round(10.6)) # 11
print(round(10.21212121)) # 10

print("----------------------------------------------------------------------------------------------------")

print(round(10.21212121, 2)) # 10.21
print(round(10.2199999, 2)) # 10.22

print("----------------------------------------------------------------------------------------------------")
