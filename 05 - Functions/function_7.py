print("----------------------------------------------------------------------------------------------------")

def nome_completo(nome, sobrenome): # OBS.: "nome" e "sobrenome" são parâmetros declarados na definição da função.
    return(f"O nome completo é {nome} {sobrenome}.")

print(nome_completo("Tiago", "Gonçalves")) # OBS.: "Tiago" e "Gonçalves", são argumentos passados na execução da função.

print("----------------------------------------------------------------------------------------------------")

nome = "Evelyn"
sobrenome = "Lysboa"

print(nome_completo(nome, sobrenome))

print("----------------------------------------------------------------------------------------------------")

print(nome_completo(nome = "Ayrton", sobrenome = "Senna"))

print("----------------------------------------------------------------------------------------------------")

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return(total)

lista = [1, 7, 6, 3, 2, 9]

print(soma_impares(lista))

print("----------------------------------------------------------------------------------------------------")
