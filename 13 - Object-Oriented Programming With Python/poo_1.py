# Programação orientada à objetos (POO)

# O POO é um paradigma de programação, que utiliza o mapeamento de objetos do mundo real para modelos computacionais.

# Paradigma de programação é a forma/metodologia pensada para desenvolver um sistema.

# Principais elementos da orientação à objetos:

"""

- Classe -> Modelo de um objeto do mundo real, sendo representado computacionalmente.
- Atributo -> Características do objeto.
- Método -> Comportamento do objeto (funções).
- Construtor -> Método especial utilizado para criar objetos.
- Objeto -> Instância de uma classe.

"""

print("----------------------------------------------------------------------------------------------------")

numero = 10

print(numero)
print(type(numero))

print("----------------------------------------------------------------------------------------------------")

nome = "Vasco"

print(nome)
print(type(nome))

print("----------------------------------------------------------------------------------------------------")

class Produto:
    pass

ps4 = Produto()

print(ps4) # Referência de endereço na memória
print(type(ps4)) # Novo tipo de dado (classe Produto)

print("----------------------------------------------------------------------------------------------------")
