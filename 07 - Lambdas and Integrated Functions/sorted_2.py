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

print(sorted(usuarios, key = lambda usuario: usuario["username"])) # Ordenando pelos usuários em ordem alfabética.

print("----------------------------------------------------------------------------------------------------")

print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True)) # Ordenando reversamente pelos usuários em ordem alfabética.

print("----------------------------------------------------------------------------------------------------")

print(sorted(usuarios, key=lambda usuario: len(usuario["threads"]))) # Ordenando pelo tamanho das Threads.

print("----------------------------------------------------------------------------------------------------")

musicas = [
    {"artista": "Nightwish", "música": "Phatom of the Opera", "execuções": 132},
    {"artista": "Avantasia", "música": "Moonglow", "execuções": 120},
    {"artista": "Angra", "música": "Carry on", "execuções": 311},
    {"artista": "Rhapsody", "música": "Down of Victory", "execuções": 560},
    {"artista": "Virgin Steele", "música": "Kingdom of the Fearless (The destruction of Troy)", "execuções": 90},
    {"artista": "Blind Guardian", "música": "Nightfall", "execuções": 235}
]

print(musicas)

print("----------------------------------------------------------------------------------------------------")

print(sorted(musicas, key=lambda musica: musica["execuções"]))

print("----------------------------------------------------------------------------------------------------")

print(sorted(musicas, key=lambda musica: musica["execuções"], reverse=True))

print("----------------------------------------------------------------------------------------------------")
