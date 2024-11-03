"""
1. Crie uma classe Pessoa, contendo nome, data de nascimento e email.
Defina as propriedades getters e setters para os atributos e um método para imprimir os dados de uma pessoa.
"""

from datetime import date

class Pessoa:
    def __init__(self, nome: str, nascimento: date, email: str) -> None: # O None é recomendado no final dos métodos construtores, para deixar claro que ele não retorna nenhum valor.
        self.__nome = nome
        self.__nascimento = nascimento
        self.__email = email
    
    @property # Os getters (utilizados nos decoradores property) são necessários para controlar o acesso e a manipulação dos atributos privados da classe de uma forma segura e organizada.
    def nome(self) -> str: # o str, indica que ele o método retorna uma string. Isso é útil para manter o código legível e consistente.
        return self.__nome
    
    @nome.setter # O setter é um método utilizado em combinação com o getter para atualizar o valor de um atributo privado (recebe um valor " nome" e atribui ao "__nome").
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def nascimento(self) -> date:
        return self.__nascimento
    
    @nascimento.setter
    def nascimento(self, nascimento: date) -> None:
        self.__nascimento = nascimento

    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email: str) -> None:
        self.__email = email

    def imprimir(self) -> None:
        print(f'Nome: {self.nome}')
        print(f'E-mail: {self.email}')
        print(f'Data Nascimento: {self.nascimento.strftime("%d/%m/%Y")}')


if __name__ == '__main__': # É usado para garantir que um certo bloco de código seja executado apenas quando o script é executado diretamente (Segurança).

    p: Pessoa = Pessoa('Indiana Jones', date(1899, 7, 1), 'indiana_jones@gmail.com') # O "p é uma abreviação da instância "Pessoa", para tornar mais legível (diferente da classe).

    print("----------------------------------------------------------------------------------------------------")

    p.imprimir()

    print("----------------------------------------------------------------------------------------------------")
