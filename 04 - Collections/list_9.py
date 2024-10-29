cores = ["verde", "amarelo", "azul", "branco"]
indice = 0

print("----------------------------------------------------------------------------------------------------")

while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

print("----------------------------------------------------------------------------------------------------")

print
for indice, cor in enumerate(cores):
    print(indice, "-", cor)

print("----------------------------------------------------------------------------------------------------")

print(cores.index("verde"))
print(cores.index("amarelo"))
print(cores.index("azul"))
print(cores.index("branco"))

# Obs.: Caso exista itens repetidos, o método "index" trará somente o primeiro valor encontrado. 
print("----------------------------------------------------------------------------------------------------")

doces = ["pudim", "pavê", "musse", "bolo", "brigadeiro", "pudim", "torta"]

print(doces.index("bolo"))
print(doces.index("pavê"))

print("----------------------------------------------------------------------------------------------------")

print(doces.index("pudim"))
print(doces.index("pudim", 1)) # Pesquisar o indice de um item a partir de um indice estipulado.
print(doces.index("pudim", 4, 6)) # Pesquisar o indice de um item a partir de range de indices estipulado.

print("----------------------------------------------------------------------------------------------------")
