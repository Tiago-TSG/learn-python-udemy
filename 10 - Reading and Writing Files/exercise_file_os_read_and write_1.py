# Programa que abre um arquivo e escreve (substituindo o conteúdo) palavras inseridas pelo usuário, até que o mesmo digite "0".
# Depois o arquivo é lido por inteiro e o seu conteúdo é impresso na tela.

with open("arq.txt", "w") as arquivo:
    while True:
       palavra = input(f"Escreva alguma coisa: ")
       if palavra != "0" :
           arquivo.write(f"{palavra}\n")
       else:
           print("----------------------------------------------------------------------------------------------------")
           print("Conteúdo adicionado ao arquivo.")
           print("----------------------------------------------------------------------------------------------------")
           break

with open("arq.txt", "r") as arquivo:
    print(f"{arquivo.read()}----------------------------------------------------------------------------------------------------")
