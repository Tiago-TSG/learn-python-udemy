# A função "StringIO", permite criar e manipular um arquivo em memória.

from io import StringIO 

# Leitura e escrita de um arquivo em memória.

print("----------------------------------------------------------------------------------------------------")

mensagem = "Apenas uma string comum."

arquivo = StringIO(mensagem)

print(arquivo.read())

print("----------------------------------------------------------------------------------------------------")

arquivo.write(" Novo texto.")

arquivo.seek(0) # Necessário voltar com o cursor para o início, para ler o arquivo novamente. Assim como em um arquivo no disco.

print(arquivo.read())

print("----------------------------------------------------------------------------------------------------")
