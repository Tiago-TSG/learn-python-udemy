import os

# Para criar arquivos

open('outro_arquivo_1.txt', 'w').close() # Função que cria um arquivo vazio e depois fecha ele.
open('outro_arquivo_2.txt', 'a').close() # Outra forma de fazer com o modo "append".


with open('outro_arquivo_3.txt', 'w') as arquivo: # Mais uma forma de obter o mesmo resultado, utilizando o bloco "with".
    pass

with open('outro_arquivo_4.txt', 'w') as arquivo: # Mais uma forma de obter o mesmo resultado, utilizando o bloco "with".
    pass

with open('outro_arquivo_5.txt', 'w') as arquivo: # Mais uma forma de obter o mesmo resultado, utilizando o bloco "with".
    pass

# Melhor forma de se criar um arquivo vazio (mais simples). Entretanto, caso o arquivo já exista, ele apresentará um erro (FileExistError).

# os.mknod('outro_arquivo_6.txt') 
# os.mknod('/home/tiago/estudos/python/geek-university/outro_arquivo_7.txt')

# Para criar diretórios

# os.mkdir("outro_dir_1") # caso o diretório já exista, ele apresentará um erro (FileExistError).
# os.mkdir("/home/tiago/estudos/python/geek-university/outro_dir_2")

# os.makedirs("package_2/sub_package_2") #  A função "makedirs()", cria toda a árvore de diretórios.

os.makedirs("package_2/sub_package_2", exist_ok=True) # A opção "exist_ok=True" ignora a existência do diretório e não apresenta erro na saída.

# Para renomear diretórios ou arquivos

# os.rename("outro_arquivo_4_1.txt", "outro_arquivo_4.txt") # Caso o arquivo não exista, ele apresentará um erro.

# os.rename("/home/tiago/estudos/python/geek-university/outro_arquivo_4_1.txt", "/home/tiago/estudos/python/geek-university/outro_arquivo_4.txt") # Outro exemplo


# Para remover arquivos # Os arquivos são deletados permanentemente. Apresenta erro, caso o arquivo não exista (FileNotFoundError).
# No caso do Windows, se um usuário estiver com o arquivo aberto, o programa também apresentará erro.

# Obs.: A função "remove()" só remove arquivos (não remove diretórios).

# os.remove("outro_arquivo_1.txt")
# os.remove("outro_arquivo_2.txt")
# os.remove("outro_arquivo_3.txt")
# os.remove("outro_arquivo_4.txt")
# os.remove("outro_arquivo_5.txt")


# Para remover diretórios vazios

os.rmdir("package_2/sub_package_2") # Obs: Não apresenta erros caso o diretório não exista mais. Somente se o diretório não estiver vazio (Directory nor empty).

# Para remover uma árvore de diretórios

os.removedirs("package_2") # Não apresenta erros caso a árvore não exista mais.


# OBS.:Com a bibliotec externa "send2trash", é possível enviar os arquivos e diretórios removidos para a lixeira. (from send2trash import send2trash)
