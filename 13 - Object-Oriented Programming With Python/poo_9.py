# Aprimorando a classe "ContaCorrente".

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'Nome: {self.__cliente._Cliente__nome} {self.__cliente._Cliente__sobrenome}\nCPF: {self.__cliente._Cliente__cpf}')

print("----------------------------------------------------------------------------------------------------")

cliente1 = Cliente('Felicity', 'Jones', '105.470.635-77')

cc1 = ContaCorrente(5000, 20000, cliente1)

cc1.mostra_cliente()

print("----------------------------------------------------------------------------------------------------")
