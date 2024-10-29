# Decorators ou decoradores, são funções que envolvem outras funções, permitindo que você altere o comportamento de uma função sem alterar seu código.
# Decorators também são exemplos de "Higher Order Functions".

# OBS: SINTAXE NÃO RECOMENDADA.

print("----------------------------------------------------------------------------------------------------")

def seja_educado(funcao): # Exemplo de "Decorator Function"
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja bem-vindo(a)!')

saudacao() # Saída sem decorador

print("----------------------------------------------------------------------------------------------------")

saudacao_decorada = seja_educado(saudacao)  # Exemplo de "Decorator"
saudacao_decorada() # Saída com decorador

print("----------------------------------------------------------------------------------------------------")


def raiva():
    print('Eu te odeio!!!!')

raiva_decorada = seja_educado(raiva)
raiva_decorada() # Saída com decorador

print("----------------------------------------------------------------------------------------------------")

# Decorators com sitaxe Sugar (açucar sintático) - RECOMENDADA!

def seja_educado_mesmo(funcao): # Exemplo de "Decorator Function"
    def sendo(*args, **kwargs): # O parâmetros "args" e "kwargs" permitem quaisquer argumentos passados para a função decoradora.
        print('Foi um prazer conhecer você!')
        funcao(*args, **kwargs)
        print('Tenha um ótimo dia!')
    return sendo

@seja_educado_mesmo # Exemplo de "Decorator"
def saudacao_amigo(nome):
    print(f'Seja bem-vindo(a) {nome}!')

saudacao_amigo('Tiago')

print("----------------------------------------------------------------------------------------------------")

