# Exemplo mais avançado

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f"Valor incorreto. O primeiro valor precisa ser igual à {valor}."
            else:
                return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

print("----------------------------------------------------------------------------------------------------")

print(comida_favorita('pizza', 'lasanha'))
print(soma_dez(10, 20))

print("----------------------------------------------------------------------------------------------------")

print(comida_favorita('macarrão', 'lasanha'))
print(soma_dez(5, 15))

print("----------------------------------------------------------------------------------------------------")
