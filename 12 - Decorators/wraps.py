# São funções que possuem utilizadas para preservar os metadados originais de outras funções, quando essas são decoradas.

from functools import wraps

def ver_log(funcao): # função decoradora
    @wraps(funcao) # Obs.: O wraps ignora os metadados da função decoradora.
    def logar(*args, **kwargs):
        """ Eu sou a função "logar", dentro de outra."""
        print(f"Chamada da função: {funcao.__name__}")
        print(f"Documentação da função: {funcao.__doc__}")
        return funcao(*args, **kwargs)
    
    return logar

@ver_log
def soma(a, b): # função original (decorada)
    """ Soma dois números. """
    return a + b

print(soma.__name__) # soma
print(soma.__doc__) # soma dois números 

# OBS.: Sem o wraps, a documentação impressa seria a da função decoradora e não a documentação. O wraps resolve esse problema, 
# mantendo os metadados da função original e não da função decoradora.
