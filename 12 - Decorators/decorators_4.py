# Forçando tipos de dados com um decorador.

print("----------------------------------------------------------------------------------------------------")

# Relembrando o Zip:

a = (1, 3, 5)
b = (2, 4, 6)

c = zip(a, b) # Retorna um objeto zip

print(tuple(c))


print("----------------------------------------------------------------------------------------------------")

# Forçando tipos de dados:

def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor)) # str(Vasco), int('3')
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador

@forca_tipo(str, int)
def repete_mensagem(msg, vezes):
    for vez in range(vezes):
        print(msg)

repete_mensagem('Vasco', '3')

print("----------------------------------------------------------------------------------------------------")

@forca_tipo(float, float)
def dividir(a, b):
    return a / b

print(dividir('1', '5'))

print("----------------------------------------------------------------------------------------------------")
