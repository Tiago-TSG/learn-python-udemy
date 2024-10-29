# Programa que abre um arquivo e conta o seu número de linhas.
# Depois imprime a quantidade de linhas existentes no arquivo.


arquivo = 'arq.txt'

with open(arquivo, "r") as arquivo:
    conteudo = arquivo.read()
    linhas = conteudo.split('\n')
    print("----------------------------------------------------------------------------------------------------")
    print(f" O arquivo '{arquivo.name}' possui {len(linhas)} linhas.")
    print("----------------------------------------------------------------------------------------------------")

# Outra forma de fazer a mesma coisa:

with open(arquivo, "r") as arquivo:
    linhas = arquivo.readlines() # OBS: o readlines() Não conta linhas em branco.
    print("----------------------------------------------------------------------------------------------------")
    print(f" O arquivo '{arquivo.name}' possui {len(linhas)} linhas.")
    print("----------------------------------------------------------------------------------------------------")
