# Métodos de classe

# Aprimorando a classe usuário, incluindo um método classe

from passlib.hash import pbkdf2_sha256 as crypt

class Usuario:

    contador = 0

    @classmethod # Decorator necessário para identificar um método de classe.
    def conta_usuarios(cls): # Exemplo de um método de classe.
        print(f'Classe: {cls}') # (Imprimindo a classe para visualização (cls é uma convenção utilizada que significa "classe".))
        print(f'Foram criados {cls.contador} usuários no sistema.')

    @staticmethod # Decorator necessário para identificar um método estático.
    def definicao():
        return(f'Usuário do sistema.')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = crypt.hash(senha, rounds=200000, salt_size=16)
            
        Usuario.contador = self.__id
            
        print(f'Usuário {self.__gera_usuario()}, criado com sucesso!')
    
    def nome_completo(self):
        return (f' {self.__nome} {self.__sobrenome}')
    
    def checa_senha(self, senha_digitada):
        if crypt.verify(senha_digitada, self.__senha):
            return True
        else:
            return False
    
    def __gera_usuario(self): # Exemplo de método privado (não pode ser acessado fora da classe), començando com duplo "underline".
        return (self.__email.split('@')[0])

print("--------------------------------------------------------------------------------------------------------------")

# Criando instâncias

user1 = Usuario('João', 'Silva', 'jsilva@gmail.com', '12345678')
user2 = Usuario('Maria', 'Santos', 'msantos@gmail.com', '654321123456')

print("--------------------------------------------------------------------------------------------------------------")

Usuario.conta_usuarios() # Forma correta de chamar um método de classe (Diretamente da classe).

print("----------------------------------------------------------------------------------------------------")

user1.conta_usuarios() # Forma incorreta de chamar um método de classe (Através de uma instância).

print("----------------------------------------------------------------------------------------------------")

user2.conta_usuarios() # Forma incorreta de chamar um método de classe (Através de uma instância).

print("--------------------------------------------------------------------------------------------------------------")

print(user1._Usuario__gera_usuario()) # Acessando um método privado de maneira não recomendada, para exibir informações de um método privado.
print(user2._Usuario__gera_usuario()) # Acessando um método privado de maneira não recomendada, para exibir informações de um método privado.

print("--------------------------------------------------------------------------------------------------------------")

# Métodos estáticos

print(user1.definicao())
print(user2.definicao())

print("--------------------------------------------------------------------------------------------------------------")
