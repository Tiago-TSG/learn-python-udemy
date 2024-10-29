# Para leitura de arquivos, utilizamos a função integrada "open()", que recebe o caminho do arquivo a ser lido.
# Essa função retorna um "_io.TextOwrapper" e é com ele que trabalhamos.

# Quando usamos a função open diretamente em um programa, é aberta uma conexão (streaming) entre o programa e o arquivo em disco.
# Para fechar essa conexão, é necessário utilizar a função "close()".

# Para mais informações sobre a função: https://docs.python.org/3/library/functions.html#open

# mode='r'  --> leitura (Padrão)

# encoding='UTF-8' --> Padrão de codificação que suporta acentuação e caracteres especiais (Atende a 99% dos casos)

# Para ler arquivos em PDF é necessário uma bibliotexa específica do Python.

print("----------------------------------------------------------------------------------------------------")

arquivo = open('arquivo_leitura.txt')

print(arquivo)
print(type(arquivo))

print("----------------------------------------------------------------------------------------------------")

# Para ler o arquivo é necessário usar a função read()

ret = arquivo.read()

print(type(ret))

print("----------------------------------------------------------------------------------------------------")

print(ret)

# OBS.: Como a leitura de arquivos no Python trabalha com cursor, se formos imprimir mais uma vez o conteúdo
# da variável arquivo, nada será exibido, já que todo o arquivo já foi lido anteriormente.

print("----------------------------------------------------------------------------------------------------")

ret = ret.split('\n') # Transforma o texto em uma lista de strings, separadas pela quebra de linhas.

print(ret)

print("----------------------------------------------------------------------------------------------------")

print(len(ret))

print("----------------------------------------------------------------------------------------------------")

arquivo.close()
