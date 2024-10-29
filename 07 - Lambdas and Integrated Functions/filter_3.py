print("----------------------------------------------------------------------------------------------------")

usuarios = [
    {"username": "tiago", "threads": ["Eu amo Pizza!", "Eu gosto de bolo também."]},
    {"username": "evelyn", "threads": ["Eu amo gato!", "Da vontade de apertar!"]},
    {"username": "bob", "threads": []},
    {"username": "daniel", "threads": ["Qual é fucker? ...", "Aí ..."]},
    {"username": "john", "threads": []}
]

print(usuarios)

print("----------------------------------------------------------------------------------------------------")

# Forma - 1

usuarios_inativos = list(filter(lambda usuario: len(usuario["threads"]) == 0, usuarios))

print(usuarios_inativos)

print("----------------------------------------------------------------------------------------------------")

# Forma - 2

usuarios_inativos = list(filter(lambda usuario: not usuario["threads"], usuarios))

print(usuarios_inativos)

print("----------------------------------------------------------------------------------------------------")

# Combinando filtros e mapas

nomes = ["Vanessa", "Ana", "Maria"]

lista_1 = list(map(lambda nome: f"Sua instrutora é a {nome}.", filter(lambda nome: len(nome) < 6, nomes)))

lista_2 = list(map(lambda nome: f"Sua instrutora é a {nome}.", filter(lambda nome: len(nome) < 5, nomes)))

print(lista_1)
print(lista_2)

print("----------------------------------------------------------------------------------------------------")
