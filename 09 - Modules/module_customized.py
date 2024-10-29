# Todo arquivo criado com código Python é um módulo customizado.
# Para importá-lo basta fazer: from "nome do arquivo" import "nome da função criada"

# OBS.: Foi necessário colocar a linha if __name__ == "__main__": para impedir a execução de outras saídas quando a importação for executada.
# O ideal é que o arquivo de origem contenha somente as funções a serem disponibilizadas para execução.

from function_2 import quadrado_de_x as qdx

print(qdx(4))


from function_1 import dar_oi

print(dar_oi())
