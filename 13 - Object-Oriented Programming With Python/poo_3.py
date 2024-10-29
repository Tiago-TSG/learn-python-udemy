# Programação orientada à objetos (POO)

"""
- Atributo -> Representam características de um objeto. Através deles, conseguimos representar computacionalnente o estado dos objetos.

"""

# Em Python os atributos são divididos em três tipos:

"""
- Atributos de Instântica --> São declarados dentro do método construtor (método utilizado para construção de objetos).
Estão presentes em todos as instâncias/objetos de uma classe.

- Atributos de Classe (estáticos) --> Possue valor comum em todas as instâncias/objetos de uma classe.

- Atributos dinâmicos. --> Podem ser criados ou deletados em tempo de execução.

"""

class Lampada:
    def __init__(self, voltagem, cor): # O __init__ é o método construtor
        self.__voltagem = voltagem # O "__" precedendo o atributo, significa que ele é privado e só pode ser acessado através da classe.
        self.__cor = cor
        self.__ligada = False

# OBS.: No Python, por convenção, ficou estabelecido que todo atributo de uma classe é público (ao contrário de outras liguagens).
# Para que seja considerado um atributo privado, é necessário utilizar o duplo underline "__" precedendo o nome do mesmo (Name Mangling).

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:
    def __init__(self, nome, email, senha): # O self (convenção) é o objeto que está executando do método.
        self.nome = nome
        self.email = email
        self.senha = senha

# OBS.: Funções dentro de uma classe são chamadas de métodos.

"""
 ps4 = Produto() # Executando o método init da classe Produto.

"""

class Cerveja:
    def __init__(cerveja, nome, idade): # Exemplo sem utilizar o objeto "self" (não recomendado)
        cerveja.nome = nome
        cerveja.idade = idade
