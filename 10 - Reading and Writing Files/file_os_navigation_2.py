import os

print("----------------------------------------------------------------------------------------------------")

# listdir() --> Cria uma lista de arquivos e diretórios do path corrente. 

os.chdir('/home/tiago/estudos/python/geek-university')

print(os.listdir())

print("----------------------------------------------------------------------------------------------------")

print(os.listdir('/home/tiago')) # Lista o conteúdo no path informado.

print("----------------------------------------------------------------------------------------------------")

print(len(os.listdir()))
print(len(os.listdir('/home/tiago'))) # Diz a quantidade dos itens no path informado.

print("----------------------------------------------------------------------------------------------------")


# Listando o conteúdo com maiores detalhes com o scandir(). É necessário fechar a conexão, assim como quando abrimos um arquivo.

scandir_iterator_1 = os.scandir('/home/tiago')

print(list(scandir_iterator_1)) # Obs: Com o scandir é necessário informar o formato do iterator (no caso, escolhi uma lista)

print("----------------------------------------------------------------------------------------------------")

scandir_iterator_2 = os.scandir('/home/tiago/estudos/python/geek-university') # Obs.: É necessário criar uma variável para receber o iterável.

arquivos = list(scandir_iterator_2)

print(arquivos)

print("----------------------------------------------------------------------------------------------------")

print(arquivos[0])

print("----------------------------------------------------------------------------------------------------")

print(dir(arquivos[0]))

print("----------------------------------------------------------------------------------------------------")

print(arquivos[0].path)

print("----------------------------------------------------------------------------------------------------")

print(arquivos[0].name)

print("----------------------------------------------------------------------------------------------------")

print(arquivos[0].inode())

print("----------------------------------------------------------------------------------------------------")

scandir_iterator_1.close() # Agora, fechamos a conexão aberta com o scandir(), utilizando a variável criada.
scandir_iterator_2.close() # Agora, fechamos a conexão aberta com o scandir(), utilizando a variável criada.
