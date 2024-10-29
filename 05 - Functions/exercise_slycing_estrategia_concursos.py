
print("----------------------------------------------------------------------------------------------------")

lista = [0, 1, 1, 2, 3, 5, 8, 13, 21]

print(lista) # [0, 1, 1, 2, 3, 5, 8, 13, 21]

print("----------------------------------------------------------------------------------------------------")

print(lista[3]) # 2
print(lista[-6]) # 2

print("----------------------------------------------------------------------------------------------------")

print(lista[2:4]) # [1, 2]

print("----------------------------------------------------------------------------------------------------")

print(lista[2:4] [-1]) # 2
print(lista[2:4] [-2]) # 1

print("----------------------------------------------------------------------------------------------------")

print(lista[1:5]) # [1, 1, 2, 3]

print("----------------------------------------------------------------------------------------------------")

print(lista[1:5] [-1]) # 3
print(lista[1:5] [-2]) # 2

print("----------------------------------------------------------------------------------------------------")

print(lista[3:]) # [2, 3, 5, 8, 13, 21]

print("----------------------------------------------------------------------------------------------------")

print(lista[3:] [-1]) # 21
print(lista[3:] [5]) # 21

print("----------------------------------------------------------------------------------------------------")

print(lista[:4]) # [0, 1, 1, 2]

print("----------------------------------------------------------------------------------------------------")

print(lista[:4] [-1]) # 2
print(lista[:4] [-2]) # 1

print("----------------------------------------------------------------------------------------------------")

print(lista[-5::]) # [3, 5, 8, 13, 21]
print(lista[-5:])  # [3, 5, 8, 13, 21]

print("----------------------------------------------------------------------------------------------------")

print(lista[-5:-2:]) # [3, 5, 8]
print(lista[-5:-2]) # [3, 5, 8]

print("----------------------------------------------------------------------------------------------------")

print(lista[-5::-2]) # [3, 1, 0]
print(lista[-1:-6:-2]) # [21, 8, 3]

print("----------------------------------------------------------------------------------------------------")

print(lista[-1::-1]) # [21, 13, 8, 5, 3, 2, 1, 1, 0]
print(lista[-1:-4:-1]) # [21, 13, 8]

print("----------------------------------------------------------------------------------------------------")

print(lista[-4:-1:-1]) # OBS: [] --> Necessário informar um intervalo positivo ou não informar (padrão=1)
print(lista[-1:-4:]) # OBS: [] --> Necessário informar o -1 pelo menos para descrescer entre um intervalo negativo
print(lista[-1:-6:]) # OBS: [] --> Necessário informar o -1 pelo menos para descrescer entre um intervalo negativo

print("----------------------------------------------------------------------------------------------------")