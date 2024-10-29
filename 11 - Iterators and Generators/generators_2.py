"""
Teste de memória com geradores
"""

# Função para gerar sequência de Fibonacci

def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(a)
        a, b = b, a + b
    return nums

print("----------------------------------------------------------------------------------------------------")

# Teste 1: Gerar lista de Fibonacci até 1000

fib_list = fib_lista(100)

print(fib_list)

# Função geradora para Fibonacci

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        yield a
        a, b = b, a + b
        contador += 1

# Teste 2: Usar gerador para Fibonacci até 100

fib_gen = fib_gen(100)

print("----------------------------------------------------------------------------------------------------")

print(fib_gen)  # Não imprime a sequência, apenas o objeto gerador

print("----------------------------------------------------------------------------------------------------")

# Iterar sobre o gerador para exibir a sequência

for num in fib_gen:
    print(num)

print("----------------------------------------------------------------------------------------------------")

# Teste 3: Comparar memória utilizada

from sys import getsizeof

# Fibonacci até 100

print(f"O tamanho da lista é: {getsizeof(fib_list)} bytes")  # 904 bytes

# Fibonacci gerador até 100

print(f"O tamanho do gerador é: {getsizeof(fib_gen)} bytes")  # 112 bytes

# O gerador não armazena todos os valores em memória, pois gera um valor por vez

"""
Neste exemplo, a lista armazena todos os valores de Fibonacci até 100, enquanto o gerador apenas gera os valores
quando são solicitados. O gerador utiliza menos memória, pois não armazena todos os valores em memória de uma vez.
"""
print("----------------------------------------------------------------------------------------------------")
