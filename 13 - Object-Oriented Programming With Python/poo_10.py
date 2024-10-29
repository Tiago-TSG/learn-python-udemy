# Programação orientada à objetos (POO)

# Abstração e Encapsulamento

"""
O grande objetivo da programação orientada a objetos é encapsular o nosso código em um grupo lógico e hierárquico, utilizando classes.


                Classe
----------------------------------------
|                                      |
|         Atributos e métodos          | 
|                                      |
----------------------------------------



# Atributos e métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado "__nome" e um método privado chamado "__falar".

Esses elementos só deveriam ser acessados dentro da classe. Mas como já visto, o Python não bloqueia o acesso fora da classe.
Podemos utilizar o recurso de "Name Mangling" para acessar esses elementos privados. 

_Classe__Elemento  (Obs.: Não recomendado)

Exemplos:

instancia._Pessoa_nome --> Acesso a um atributo privado.

instancia._Pessoa_falar()  --> Acesso a um método privado.

"""

# Abstração em POO, é o ator de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados de usuário.

class Conta:

    contador = 1000

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo do titular {self.__titular} é R${self.__saldo} e seu limite é de R${self.__limite}.')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo.')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente.')
        else:
            print('O valor precisa ser positivo.')

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor

        conta_destino.__saldo += valor


print("----------------------------------------------------------------------------------------------------")

print("ANTES DA TRANSFERÊNCIA")

print("----------------------------------------------------------------------------------------------------")

conta1 = Conta('Nestinho', 30000, 3000)
conta1.extrato()

conta2 = Conta('Luluzinha', 500, 1000)
conta2.extrato()

print("----------------------------------------------------------------------------------------------------")

print("APÓS DA TRANSFERÊNCIA")

print("----------------------------------------------------------------------------------------------------")

conta1.transferir(5000, conta2)

conta1.extrato()
conta2.extrato()

print("----------------------------------------------------------------------------------------------------")
