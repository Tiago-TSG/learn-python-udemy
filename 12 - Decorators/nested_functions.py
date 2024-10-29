# Inner functions ou Nested functions são funções dentro de outras funções.
# Elas podem acessar o escopo de funções mais externas.

from random import choice

print("----------------------------------------------------------------------------------------------------")

def cumprimento(pessoa):
    def humor():
        return choice(('E aí!', 'Olá!', 'Tudo bem?', 'Como vai?', 'Opa!', 'Tudo ótimo!'))
    return pessoa + '. ' + humor()

print(cumprimento('Tiago'))


# Retornando funções de outras funções

def faz_me_rir():
    def rir():
        return choice(('KKKKKKKKKK', 'Hahaha', 'Hehehe', 'Hihihi'))
    return rir

rindo = faz_me_rir()

print(rindo())

print("----------------------------------------------------------------------------------------------------")
