# Comprehension --> [dado for dado in iterável]

numeros = [1, 2, 3, 4, 5]

print("----------------------------------------------------------------------------------------------------")

numeros_multiplicados = [n * 10 for n in numeros] 

print(numeros_multiplicados) # [10, 20, 30, 40, 50]

print("----------------------------------------------------------------------------------------------------")

numeros_divididos = [n / 2 for n in numeros]

print(numeros_divididos) # [0.5, 1.0, 1.5, 2.0, 2.5]

print("----------------------------------------------------------------------------------------------------")

def funcao(valor):
    return(valor ** (1/2))

numeros_raiz = [funcao(n) for n in numeros]

print(numeros_raiz) # [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979]

print("----------------------------------------------------------------------------------------------------")