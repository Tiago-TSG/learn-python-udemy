print("----------------------------------------------------------------------------------------------------")

paises = ["", "Argentina","", "Russia", "Italia","", "Brasil", "Chile", "Peru", "Portugal", "Bolivia","Japão"]

print(paises)

print("----------------------------------------------------------------------------------------------------")

# Formato - 1

paises_filtrados = filter(lambda pais: len(pais) > 0, paises)

print(list(paises_filtrados))

# Formato - 2

paises_filtrados = filter(lambda pais: pais != "", paises)

print(list(paises_filtrados))

# Formato - 3

paises_filtrados = filter(None, paises) # Não entendi muito bem, mais o "None" aqui funciona como um filtro inverso. Tudo que não for vazio é retornado.

print(list(paises_filtrados))

print("----------------------------------------------------------------------------------------------------")
