# OBS: Assinatura de uma função é representada pelo seu retorno, nome e parâmetros de entrada (ex: *args, **kwargs)

# Outro exemplo de função decoradora:

def gritar(funcao):
    def aumentar(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        return resultado.upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, meu nome é o/a {nome}!'

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} com {acompanhamento}.'

print(saudacao('Evelyn'))
print(ordenar('X-burguer', 'fritas'))

print("----------------------------------------------------------------------------------------------------")

# OBS.: Vale lembrar que podemos nomear os parâmetros de entrada da função decoradora, e assim, 
# podemos passar argumentos para a função decorada.

print(ordenar(acompanhamento='X-buguer', principal='fritas'))

print("----------------------------------------------------------------------------------------------------")
