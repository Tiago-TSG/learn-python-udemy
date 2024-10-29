# Em Python, o dunder é utilizado para criar funções, atributos, propriedas, etc..., 
# sem gerar conflito com o nome desses elementos na programação.

# Dunder --> Doble Under
# Dunder Name --> __name__
# Dunder Main --> __main__

# Em Python, se executarmos um módulo (arquivo) diretamente da linha de comando, automaticamente, 
# o Python atribuirá à variable "__name__" o valor "__main__" , indicando que esse módulo é o de execução principal.

# Exemplo utilização:

def dar_oi(): 
    return  ("Oi!")

if __name__ == "__main__": # Daqui para o final do arquivo, só será executado se o arquivo "dunder.py" for executado diretamente.

    
    print("----------------------------------------------------------------------------------------------------")

    print(dar_oi())

    print("----------------------------------------------------------------------------------------------------")

    print("Vasco da Gama")

    print("----------------------------------------------------------------------------------------------------")

else:
    print(f"O módulo '{__name__}' foi importado com sucesso!")  # A variável "__name__" exibirá o nome do módulo quando importado.
    
# Caso o arquivo não seja executado diretamente, ao final da execução do módulo, será apresentada a mensagem acima.
