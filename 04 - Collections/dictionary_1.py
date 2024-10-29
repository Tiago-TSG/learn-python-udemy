paises_1 = {"br": "Brasil", "eua": "Estados Unidos", "pt": "Portugal", "jp": "Japão", "uk": "Reino Unido"}

print("----------------------------------------------------------------------------------------------------")

print(type(paises_1))

print("\n")

print(paises_1)

paises_2 = dict(ar= "Argentina", eua= "Estados Unidos", jp= "Japão", bg= "Bulgária", cu= "Cuba", it= "Itália")

print("----------------------------------------------------------------------------------------------------")

print(type(paises_2))

print("\n")

print(paises_2)

print("----------------------------------------------------------------------------------------------------")

print(paises_1["br"])
print(paises_2["it"])
print(paises_1["eua"])
print(paises_1["jp"])

print("----------------------------------------------------------------------------------------------------")

# print(paises_1["ru"]) # Traz um keyError, por não existir a chave informada.
print(paises_2.get("ru")) # Forma recomendada para selecionar um dado de um dicionário (ou mapa) --> Se não existir, apresenta um Tipo "None".

pais_inexistente = paises_2.get("ru")
print(pais_inexistente)

print("----------------------------------------------------------------------------------------------------")
