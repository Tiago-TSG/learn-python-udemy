# O Try e o except são utilizados para tratar problemas de código que podem ocorrer, não impedindo a execução do programa em caso de algum problema.

try:
    funcao_qualquer() # Chamando uma função que não existe, para simular um problema no código.
except:
    print("----------------------------------------------------------------------------------------------------")
    print("O correu algum problema.")
    print("----------------------------------------------------------------------------------------------------")


try:
    len(5) # OBS.: Não se pode utilizar o len com números inteiros.
except:
    print("O correu algum problema.")
    print("----------------------------------------------------------------------------------------------------")

# OBS.:Tratar os erros de forma genérica, não é a melhor forma de se tratar erros. O ideal é tratar sempre de forma específica.

try:
    funcao_qualquer()
except NameError:
    print("Você está utilizando uma função inexistente.")
    print("----------------------------------------------------------------------------------------------------")

try:
    funcao_qualquer()
except TypeError:  # OBS.: Neste caso, o erro irá explodir na tela. Já que, o tipo de erro informado é diferente do tipo "NameError"
    print("Você está utilizando uma função inexistente.")
    print("----------------------------------------------------------------------------------------------------")
