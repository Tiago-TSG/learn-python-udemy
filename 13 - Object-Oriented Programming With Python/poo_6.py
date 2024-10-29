# Aprimorando a classe usuário, incluindo um novo método de instância para criptografar a senha dos usuários.

from passlib.hash import pbkdf2_sha256 as crypt

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = crypt.hash(senha, rounds=200000, salt_size=16)
    
    def nome_completo(self):
        return (f' {self.__nome} {self.__sobrenome}')
    
    def checa_senha(self, senha_digitada):
        if crypt.verify(senha_digitada, self.__senha):
            return True
        else:
            return False
        
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ') 
email = input('Digite seu email: ')

senha = input('Digite sua senha: ')
confirma_senha = input('Confirme sua senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('As senhas não coincidem!')
    exit()

print(f'Bem-vindo, {user.nome_completo()}!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso liberado!')
else:
    print('Acesso negado!')

print("--------------------------------------------------------------------------------------------------------------")

print(f'Senha critografada: {user._Usuario__senha}') # Forma errada de exibir dados ocultos. Somente para mostrar a senha criptografada.

print("--------------------------------------------------------------------------------------------------------------")
