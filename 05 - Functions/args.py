print("----------------------------------------------------------------------------------------------------")

def soma_numeros(*args):
    print(args)

soma_numeros()
soma_numeros(1, 4, 8)
soma_numeros(0, 3, 6, 8, 10)

print("----------------------------------------------------------------------------------------------------")

def soma_numeros(*args):
    total = 0
    for n in args:
        total = total + n
    return (total)

print(soma_numeros(0, 1, 2, 5, 9))

print("----------------------------------------------------------------------------------------------------")

def soma_numeros_simplificada(*args):
    return(sum(args))

print(soma_numeros_simplificada(0, 10, 15, 25, 50))

print("----------------------------------------------------------------------------------------------------")

def verifica_cores(*args):
    if "verde" in args and "amarelo" in args and "azul" in args:
        return("É Brasil, porra!!!")
    else:
        return("Tá faltando cor!")

print(verifica_cores(1.222, "verde", "azul", "laranja", 1, 3, 4))
print(verifica_cores(1.222, "verde", "amarelo", "azul", 1, 3, 4))

print("----------------------------------------------------------------------------------------------------")

def soma_numeros_lista(*args):
    return(sum(args))

lista = [0, 10, 15, 25, 50]

print(soma_numeros_lista(*lista)) # Necessário o "*" no início da lista, para desempacotar os números (se não a lista completa seria tratada como um único elemento).

print("----------------------------------------------------------------------------------------------------")
