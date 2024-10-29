musicas = [
    {"artista": "Nightwish", "música": "Phatom of the Opera", "execuções": 132},
    {"artista": "Avantasia", "música": "Moonglow", "execuções": 120},
    {"artista": "Angra", "música": "Carry on", "execuções": 311},
    {"artista": "Rhapsody", "música": "Down of Victory", "execuções": 560},
    {"artista": "Virgin Steele", "música": "Kingdom of the Fearless (The destruction of Troy)", "execuções": 90},
    {"artista": "Blind Guardian", "música": "Nightfall", "execuções": 235}
]

print("####################################################################################################")

print(min(musicas, key= lambda musica: musica["execuções"]))

print("----------------------------------------------------------------------------------------------------")

print(min(musicas, key= lambda musica: musica["execuções"]).values())

print("----------------------------------------------------------------------------------------------------")

print(list(min(musicas, key= lambda musica: musica["execuções"]).values()))

print("####################################################################################################")

print(max(musicas, key= lambda musica: musica["execuções"]))

print("----------------------------------------------------------------------------------------------------")

print(max(musicas, key= lambda musica: musica["execuções"]).values())

print("----------------------------------------------------------------------------------------------------")

print(list(max(musicas, key= lambda musica: musica["execuções"]).values()))

print("####################################################################################################")
