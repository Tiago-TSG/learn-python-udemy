print("----------------------------------------------------------------------------------------------------")

def gera_funcao_quadratica(a, b, c):
    return(lambda x: a * x ** 2 + b * x + c)

teste = gera_funcao_quadratica (2, 5, 8)

print(teste(1))
print(teste(3))
print(teste(10))

print("----------------------------------------------------------------------------------------------------")

print(gera_funcao_quadratica(2, 5, 8)(1))
print(gera_funcao_quadratica(2, 5, 8)(3))
print(gera_funcao_quadratica(2, 5, 8)(10))

print("----------------------------------------------------------------------------------------------------")
