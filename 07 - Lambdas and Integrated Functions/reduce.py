# funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
# Ou seja, a cada passo, ele execulta a função recebendo como primeiro elemento o resultado da execução anterior.

#  Precisa de dois parâmetros para operar (ao contrário do "map" e do "filter", que operam com 1 ou mais parâmetros) 

# funcao(a1*a2)
# funcao((a1*a2), a3)
# funcao((a1*a2), a3), a4)
# etc...

print("----------------------------------------------------------------------------------------------------")

numeros = [1, 3, 5, 7, 9]

# Utilizando o loop "FOR"

resultado = 1

for n in numeros:
    resultado = resultado * n

print(resultado) # 945

print("----------------------------------------------------------------------------------------------------")

# Trabalhando com o a função reduce() que não é mais integrada (built-in), desde a versão 3.0 do Python

from functools import reduce

multiplicador = lambda x, y: x * y

resultado = reduce(multiplicador, numeros)

print(resultado) # Obs.: A operação é semelhante ao "for" utilizado logo acima.

print("----------------------------------------------------------------------------------------------------")
