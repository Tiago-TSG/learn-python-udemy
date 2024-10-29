# O "with" é utilizado para criar um contexto de utilização de funções para leitura de arquivos,
# onde no final, todos os recursos são fechados/encerrados.
# É a forma Pythônica de se trabalhar com arquivos.

print("----------------------------------------------------------------------------------------------------")

with open('arquivo.txt') as arquivo:
    print(arquivo.readlines())
    print("----------------------------------------------------------------------------------------------------")
    print(arquivo.closed)

print("----------------------------------------------------------------------------------------------------")

# Qualquer tentativa de manipulação do arquivo após o bloco "with" terá problemas, 
# já que o arquivo é fechado após utilização no bloco.

print(arquivo.closed)

print("----------------------------------------------------------------------------------------------------")

# Exemplo de erro ao se executar uma leitura após o bloco "with" se encerrar.

print(arquivo.read())
