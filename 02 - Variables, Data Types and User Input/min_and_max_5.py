musicas = [
    {"artista": "Nightwish", "título": "Phatom of the Opera", "execuções": 132},
    {"artista": "Avantasia", "título": "Moonglow", "execuções": 120},
    {"artista": "Angra", "título": "Carry on", "execuções": 311},
    {"artista": "Rhapsody", "título": "Down of Victory", "execuções": 560},
    {"artista": "Virgin Steele", "título": "Kingdom of the Fearless (The destruction of Troy)", "execuções": 90},
    {"artista": "Blind Guardian", "título": "Nightfall", "execuções": 235}
]

print("####################################################################################################")

print(f"A música menos tocada foi a '{min(musicas, key= lambda musica: musica['execuções'])['título']}' da banda '{min(musicas, key= lambda musica: musica['execuções'])['artista']}'.")

print(f"A música mais tocada foi a '{max(musicas, key= lambda musica: musica['execuções'])['título']}' da banda '{max(musicas, key= lambda musica: musica['execuções'])['artista']}'.")

print("####################################################################################################")

# DESAFIO SEM UTILIZAR MAX, MIN E LAMBDA

max = 0

for musica in musicas:
    if musica['execuções'] > max:
        max = musica['execuções']

for musica in musicas:
    if musica['execuções'] == max:
        print(f"A música mais tocada foi a '{musica['título']}', da banda '{musica['artista']}'.")

min = 999999999999

for musica in musicas:
    if musica['execuções'] < min:
        min = musica['execuções']

for musica in musicas:
    if musica['execuções'] == min:
        print(f"A música menos tocada foi a '{musica['título']}', da banda '{musica['artista']}'.")

print("####################################################################################################")
