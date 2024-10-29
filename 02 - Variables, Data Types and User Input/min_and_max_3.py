print("----------------------------------------------------------------------------------------------------")

print(max("a", "f", "g", "w", "c")) # O "w" está mais a frente no alfabeto

print(max("a", "fd", "ge", "bzsqw", "vz")) # O "v" está mais a frente no alfabeto (OBS.:verifica a primeira letra primeiro e depois os demais caracteres)

print(max("z", "fd", "ge", "aasqw", "aw")) # O "z" está mais a frente no alfabeto

print("----------------------------------------------------------------------------------------------------")

print(max("Vasco da Gama")) # s

print("----------------------------------------------------------------------------------------------------")

nomes = ["Tiago", "Evelyn", "Daniel", "Vivi"]

print(max(nomes)) # Vivi
print(min(nomes)) # Daniel

print("----------------------------------------------------------------------------------------------------")

print(max(nomes, key=lambda nome: len(nome))) # OBS.: Entre Daniel e Evelyn, como o "E" está na frente no alfabeto, o nome "Evelyn" é maior.

print("----------------------------------------------------------------------------------------------------")

print(min(nomes, key=lambda nome: len(nome))) # Vivi

print("----------------------------------------------------------------------------------------------------")
