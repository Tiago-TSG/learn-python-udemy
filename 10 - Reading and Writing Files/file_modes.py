# Modos de abertura de arquivos com o Python:

# 'r' --> Modo de leitura.
# 'w' --> Mode de escrita.
# 'x' --> Abre para escrita somente se o arquivo não existir. Caso o arquivo exista, será gerado um erro (FileExistsError).
# 'a' --> Abre o arquivo no modo append, adicionando novos itens ao invés de substituir o arquivo.
# '+' --> Abre para o modo de atualização: Leitura e Escrita. Possibilita o controle do cursor.

# https://docs.python.org/3/library/functions.html#open

print("----------------------------------------------------------------------------------------------------")

try:
    with open("arquivo_escrita_1.txt", "x") as arquivo:
        arquivo.write("Tentando criar um arquivo novo. \n")
except FileExistsError:
    print(f"O arquivo já existe.")

print("----------------------------------------------------------------------------------------------------")

try:
    with open("arquivo_escrita_4.txt", "a") as arquivo_frutas:
        while True:
            fruta = input("Digite uma fruta ou digite sair: ")
            if fruta != "sair":
                arquivo_frutas.write(f'{fruta}\n')
            else:
                print("Arquivo para compra de frutas finalizado.")
            break
except FileExistsError:
    print(f"O arquivo já existe.")

print("----------------------------------------------------------------------------------------------------")
