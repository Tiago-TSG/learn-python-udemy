# Programação orientada à objetos (POO)

"""
- Método -> Representam o comportamento dos objetos (funções) ou ações que os mesmos podem realizar em um sistema.
"""

# Em Python, os métodos são divididos em dois grupos:

"""
- Metodos de instância
- Métodos de Classe
"""

# O método dunder init (__init__) é um método especial chamado de construtor e sua função é construir objetos a partir da classe.
# Não é recomendado criar métodos dunder, pois são métodos "builtin" da própria linguagem Python.

# OBS.: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline).
# OBS.: Os métodos/funções dunder em Python são chamados de métodos mágicos.
# Obs.: Os métodos devem possuir letras minúsculas, e em caso de palavras compostas, devem ser separados por underline.

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:
    
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id
    
    def desconto(self, porcentagem):
        """Retorna o valor do produto com desconto"""
        return(self.__valor * (100 - porcentagem))/100
    
class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
    
    def nome_completo(self):
        return (f' {self.__nome} {self.__sobrenome}')


print("----------------------------------------------------------------------------------------------------")

# Métodos de instância (são necessários quando se quer acessar atributos de instâncias):

p1 = Produto('Playstation 4', 'Video Game', 2300)

print(p1.desconto(20)) # self = p1

print(Produto.desconto(p1, 30)) # Outra forma de fazer (self, desconto)

print("----------------------------------------------------------------------------------------------------")

user1 = Usuario('Tiago', 'Gonçalves', 'tiago@gmail.com', '12356')
user2 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '654321')

print(user1.nome_completo()) # self = user1
print(user2.nome_completo()) # self = user2

# Outra forma de fazer

print(Usuario.nome_completo(user1)) # self = user1
print(Usuario.nome_completo(user2)) # self = user2

print("----------------------------------------------------------------------------------------------------")
