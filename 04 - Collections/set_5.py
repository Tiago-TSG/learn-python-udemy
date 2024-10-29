s = {1, 2, 3, 4, 5}


print("----------------------------------------------------------------------------------------------------")

print(s)

s.add(6)
print(s)

s.remove(1)
print(s) # Caso o valor que se quer remover não exista, é apresentado um "keyError"

s.discard(6) # O método discard também remove um número de um conjunto, mas ignora, caso tentemos remover um número que não existe.
print(s)

print("----------------------------------------------------------------------------------------------------")

print(s)

novo = s.copy() # Deep Copy
print(novo)

novo.add(6)
print(s)
print(novo)

print("----------------------------------------------------------------------------------------------------")

novo = s # Shallow Copy
print(s)
print(novo)

novo.add(6)
print(s)
print(novo)

print("----------------------------------------------------------------------------------------------------")

novo.clear()
print(novo)

print("----------------------------------------------------------------------------------------------------")
