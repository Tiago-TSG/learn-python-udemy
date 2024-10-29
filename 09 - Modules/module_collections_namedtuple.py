from collections import namedtuple

#cachorro = namedtuple("cachorro", "nome" "raça" "idade") # Forma - 1

#cachorro = namedtuple("cachorro", "nome", "raça", "idade") # Forma - 2

print("----------------------------------------------------------------------------------------------------")

cachorro = namedtuple("cachorro", ["nome", "raça", "idade"]) # Forma - 3 (RECOMENDADA)

cachorro_1 = cachorro(nome= "Mel", raça= "Viralata", idade= 6)

print(cachorro_1)

print("----------------------------------------------------------------------------------------------------")

# Acessando dados via forma padrão (tuplas)

print(cachorro_1.index("Mel"))
print(cachorro_1.index("Viralata"))
print(cachorro_1.index(6))

print("----------------------------------------------------------------------------------------------------")

print(cachorro_1[0])
print(cachorro_1[1])
print(cachorro_1[2])

print("----------------------------------------------------------------------------------------------------")

# Acessando dados via declaração da variável no namedtuple (Mais fácil de utilizar)

print(cachorro_1.nome)
print(cachorro_1.raça)
print(cachorro_1.idade)

print("----------------------------------------------------------------------------------------------------")
