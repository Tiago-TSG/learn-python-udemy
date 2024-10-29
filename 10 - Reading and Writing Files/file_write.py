# Quando se abre um arquivo para escrita, não se pode ler o arquivo, apenas escrever.
# Assim como, quando se abre um arquivo para leitura, não se pode escrever no arquivo.
# Por padrão a função open() abre um arquivo no modo leitura (r)

# Para escrever em um arquivo, utiliza-se a função "write()". Ela recebe uma string como parâmetro.

with open('arquivo_escrita.txt', 'w') as arquivo:
    arquivo.write("Testando escrita de arquivos, com o Python. \n")
    arquivo.write("Parece muito interessante.")

# Obs.: Caso o arquivo não exista, ele será automaticamente criado. Caso ele já exista, ele será sobreescrito.

# Forma mais comum e não Pythônica de ser escrever em arquivos.

arquivo = open("arquivo_escrita_2.txt", "w")

arquivo.write("Testando a escrita em arquivos de forma não Pythônica.\n")
arquivo.write("Parece simples.")

arquivo.close()

# Outras formas de se trabalhar com escritas em arquivos:

with open("arquivo_escrita_3.txt", "w") as arquivo_time:
    arquivo_time.write("Vasco \n" * 100)

# Uma forma mais complexa:

with open("arquivo_escrita_4.txt", "w") as arquivo_frutas:
    while True:
        fruta = input("Digite uma fruta ou digite sair: ")
        if fruta != "sair":
            arquivo_frutas.write(f'{fruta}\n')
        else:
            print("Arquivo para compra de frutas finalizado.")
            break
            