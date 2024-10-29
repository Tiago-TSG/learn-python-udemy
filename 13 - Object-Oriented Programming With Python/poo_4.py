
# Exemplificando atributos públicos e privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

user = Acesso('user@gmail.com', '123456')

print("----------------------------------------------------------------------------------------------------")

print(user.email) #user@gmail.com
print(user._Acesso__senha) # OBS.: Apesar de não ser recomedando, conseguimos acessar atributos privados no Python com "_Class__atributo" (123456).

print("----------------------------------------------------------------------------------------------------")

# Exemplificando Atributos de Instância (Estão presentes em todos os objetos de uma classe):

user1 = Acesso('user1@gmail.com', '123456')
user2 =  Acesso('user2@gmail.com', 'abcdefgh')

# Exemplificando Atributos de Classe (São declarados na Classe e possuem valores comuns às todas as instâncias/objetos)

class ProdutoNovo:
    
    imposto = 1.05 # 5% de imposto
    contador = 0

    def __init__(self, nome, marca, valor):
        self.id = ProdutoNovo.contador + 1
        self.nome = nome
        self.marca = marca
        self.valor = (valor * ProdutoNovo.imposto)
        ProdutoNovo.contador = self.id

p1 = ProdutoNovo('Playstation 4', 'Sony', 2500)
p2 = ProdutoNovo('Xbox One', 'Microsoft', 3000)

print(p1.imposto) # 1.05
print(p2.imposto) # 1.05

print(ProdutoNovo.imposto) # Forma recomendada de acessar um atributo de classe (1.05).

print("----------------------------------------------------------------------------------------------------")

print(p1.valor) # 2625.0
print(p2.valor) # 3150.0

print("----------------------------------------------------------------------------------------------------")

print(p1.id)
print(p2.id)

print("----------------------------------------------------------------------------------------------------")

# Exemplificando Atributos Dinâmicos

p2.peso = '5kg' # Na classe do produto não existe o atributo peso, porém, é possível adicionar dinamicamente.

print(f'Produto = {p2.nome} | Marca = {p2.marca} | Valor = {p2.valor} | Peso = {p2.peso}')

print("----------------------------------------------------------------------------------------------------")

print(p1.__dict__)
print(p2.__dict__)

print("----------------------------------------------------------------------------------------------------")

del p2.peso # Apagando o atributo dinâmico peso.

print(p1.__dict__)
print(p2.__dict__)

print("----------------------------------------------------------------------------------------------------")
