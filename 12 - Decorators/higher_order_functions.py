# Funções de maior grandeza (HOF), são funções que retornam outras funções como resultado,
# ou que recebem funções como argumentos ou até mesmo que criam variáveis do tipo função em nossos programas.

print("----------------------------------------------------------------------------------------------------")

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def calculadora(operacao, a, b):
    return operacao(a, b)

print(calculadora(soma, 2, 3)) # 5
print(calculadora(subtracao, 2, 3)) # -1
print(calculadora(multiplicacao, 2, 3)) # 6
print(calculadora(divisao, 2, 3 )) # 0.66666666

print("----------------------------------------------------------------------------------------------------")

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2)) # 2*2 = 4
print(triplicar(2)) # 2*3 = 6
print(quadruplicar(2)) # 2*4 = 8

print("----------------------------------------------------------------------------------------------------")
