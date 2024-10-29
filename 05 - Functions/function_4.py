print("----------------------------------------------------------------------------------------------------")

def time():
    time = "Vasco"
    if time == "Vasco":
        return("É gol!")
    elif time == "Flamengo":
        return("Mulambada!")
    return("Time errado!")

print(time())

print("----------------------------------------------------------------------------------------------------")

def lista_numeros():
    return 1, 2, 3, 4, 5

print(type(lista_numeros()))
print(lista_numeros())

num1, num2, num3, num4, num5 = lista_numeros()

print("----------------------------------------------------------------------------------------------------")

print(num1)
print(num2)
print(num3)
print(num4)
print(num5)

print("----------------------------------------------------------------------------------------------------")

print([num5, num2, num3, num4, num5])
print({num1, num2, num3, num4, num5})

print("----------------------------------------------------------------------------------------------------")

print(list(lista_numeros()))
print(set(lista_numeros()))

print("----------------------------------------------------------------------------------------------------")
