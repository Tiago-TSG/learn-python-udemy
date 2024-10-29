print("----------------------------------------------------------------------------------------------------")

def max_number():
    lista = []
    count = 10

    while len(lista) < count:
        numero = int(input("Digite um número inteiro: "))
        lista.append(numero)
    print("----------------------------------------------------------------------------------------------------")
    return(f'O maior número digitado foi o "{max(lista)}".')
    


print(max_number())

print("----------------------------------------------------------------------------------------------------")
