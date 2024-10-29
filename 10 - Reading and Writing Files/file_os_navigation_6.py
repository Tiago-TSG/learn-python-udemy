import os
import tempfile

# Trabalhando com diretórios e arquivos temporários

with tempfile.TemporaryDirectory() as tmp:
    print(f"Criei o diretório temporário {tmp}")
    with open(os.path.join(tmp, "arquivo_temporario.txt"), "w") as arquivo:
        arquivo.write("Vasco da Gama")
    input() # O input serve para segurar o arquivo criado temporariamente até o cancelamento da execução do código.


# Para criação de arquivos, utilizamos a seguinte função:

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Vasco da Gama\n') # Precisamos utilizar o "b", pois a escrita em arquivos temporários é feita de forma binária.
    tmp.seek(0)
    print(tmp.read())


# Outra forma de fazer o mesmo:

arquivo = tempfile.TemporaryFile()

arquivo.write(b"Vasco da Gama\n")
arquivo.seek(0)
print(arquivo.read())
arquivo.close()


# Outra forma de fazer o mesmo:

arquivo = tempfile.NamedTemporaryFile()

arquivo.write(b"Vasco da Gama\n")
arquivo.seek(0)
print(arquivo.read())
print(arquivo.name) # Informa o path do arquivo
input() # O input serve para segurar o arquivo criado temporariamente até o cancelamento da execução do código.
arquivo.close()

# Para mais informações sobre o módulo OS: https://docs.python.org/pt-br/3/library/os.html
