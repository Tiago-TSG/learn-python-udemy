print("----------------------------------------------------------------------------------------------------")

arquivo = open('arquivo_leitura.txt')

print(arquivo)
print(type(arquivo))

print("----------------------------------------------------------------------------------------------------")

print(arquivo.read())

print("----------------------------------------------------------------------------------------------------")

arquivo.seek(0) # OBS.: Com o seek, conseguimos manipular o cursor do arquivo para o início do texto, e imprimí-lo novamente.

print(arquivo.read())

print("----------------------------------------------------------------------------------------------------")

arquivo.seek(44)

print(arquivo.read())

print("----------------------------------------------------------------------------------------------------")

arquivo.seek(0)

print(arquivo.readline()) # Imprime somente a primeira linha.
print(arquivo.readline()) # Como o cursor passou para o início da segunda linha, imprime somente a segunda linha.
print(arquivo.readline()) # Como o cursor passou para o início da terceira linha, imprime somente a terceira linha.

print("----------------------------------------------------------------------------------------------------")

arquivo.seek(0) # Obs.: É necessário que o cursos esteja no início do texto.

print(arquivo.readlines()) # A função readlines() cria uma lista de strings contendo todas as linhas do texto.

print("----------------------------------------------------------------------------------------------------")

arquivo.seek(0) # Obs.: É necessário que o cursos esteja no início do texto.

print(len(arquivo.readlines()))

print("----------------------------------------------------------------------------------------------------")

arquivo.seek(0) # Obs.: É necessário que o cursos esteja no início do texto.
print(arquivo.read(6)) # O "6" determina que a função read() só fará a leitura até a posição "6".

print("----------------------------------------------------------------------------------------------------")

print(arquivo.closed) # Verifica se o arquivo encontra-se fechado ou aberto. Se "True", fechado, se "False", aberto.

arquivo.close()

print(arquivo.closed) # Após fechar o arquivo, a função retorna "True".

# OBS.: Para qualquer nova manipulação no arquivo, se faz necessário abrir novamente com a função "open()".
 
print("----------------------------------------------------------------------------------------------------")
