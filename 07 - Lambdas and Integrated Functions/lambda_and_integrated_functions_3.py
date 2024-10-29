autores = ["Morfydd Clark", "Robert Aramayo", "Antonio Te Maioha", "Sophia Nomvete", "Charlie Vickers", "Ismael Cruz Córdova", "Maxim Baldry", "Tyroe Muhafidin", "Nazanin Boniadi"]

print("----------------------------------------------------------------------------------------------------")

print(autores)

print("----------------------------------------------------------------------------------------------------")

autores.sort() # Ordena pelo nome do autor.

print(autores)

print("----------------------------------------------------------------------------------------------------")

autores.sort(key = lambda sobrenome: sobrenome.split(" ")[-1]) # Ordena pelo sobrenome do autor.

print(autores)

print("----------------------------------------------------------------------------------------------------")
