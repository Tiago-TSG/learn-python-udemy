# Programação orientada à objetos (POO)

"""
- Objetos -> São instâncias de uma classe. Ou seja, o mapeamento de um objeto do mundo real para sua representação computacional.
Devemos poder criar, quantos objetos/instâncias forem necessárias. São como variáveis de um tipo definido pela classe.
"""

class Lampada:
    def __init__(self, cor, voltagem, lumiosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = lumiosidade
        self.__ligada = False
    
    def checa_lampada(self):
        return self.__ligada
    
    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True
    
class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

    def nome_completo(self):
        return (f' {self.__nome} {self.__sobrenome}')

print("----------------------------------------------------------------------------------------------------")

# Instâncias/Objetos

lamp1 = Lampada('branca', 110, 60)
print(f'A lâmpada está ligada: {lamp1.checa_lampada()}')

lamp1.ligar_desligar()
print(f'A lâmpada está ligada: {lamp1.checa_lampada()}')

lamp1.ligar_desligar()
print(f'A lâmpada está ligada: {lamp1.checa_lampada()}')

print("----------------------------------------------------------------------------------------------------")

cc1 = ContaCorrente(5000, 20000) # Exemplo de instância da classe "ContaCorrente".


user1 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

print(user1.nome_completo())

print("----------------------------------------------------------------------------------------------------")

nome = 'Napoleão'
sobrenome = 'Bonaparte'
email = 'nb@gmail.com'
senha = '654321'

user2 = Usuario(nome, sobrenome, email, senha)

print(Usuario.nome_completo(user2))

print("----------------------------------------------------------------------------------------------------")
