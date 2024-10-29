from collections import Counter

letras = ["a", "b", "c", "c" , "c", "c", "d", "e", "f", "f", "f", "g", "g", "h", "h", "h", "h", "h", "i", "i"]

print("----------------------------------------------------------------------------------------------------")

res_counter_letras = Counter(letras)
print(res_counter_letras)
print(type(res_counter_letras))


time = ("Vasco da Gama")

print("----------------------------------------------------------------------------------------------------")

res_counter_time = Counter(time)
print(res_counter_time)
print(type(res_counter_time))

print("----------------------------------------------------------------------------------------------------")

a_lenda_da_serpente = """Conta a lenda que uma vez uma serpente começou a perseguir um vaga-lume. Este, fugia rápido, com medo da feroz predadora, 
e a serpente nem pensava em desistir. Fugiu um dia e ela não desistia, dois dias e nada...

No terceiro dia, já sem forças, o vaga-lume parou e disse a serpente:
- Posso lhe fazer três perguntas?
- Não costumo abrir esse precedente a ninguém, mas já que vou te devorar mesmo, pode perguntar...
- Pertenço a sua cadeia alimentar?
- Não.
- Eu te fiz algum mal?
- Não
- Então, por que você quer acabar comigo?
- Porque não suporto ver você brilhar...

Moral da história:
Têm pessoas que se dizem seu(a) amigo(a), mas o que eles querem mesmo é acabar
com o seu(a) sucesso."""

print(len(a_lenda_da_serpente)) # Quantidade de letras do texto.

print("----------------------------------------------------------------------------------------------------")

print(a_lenda_da_serpente.split())  # Lista de palavras do texto.

print("----------------------------------------------------------------------------------------------------")

print(len(a_lenda_da_serpente.split())) # Quantidades de palavras do texto.

print("----------------------------------------------------------------------------------------------------")

print(Counter(a_lenda_da_serpente.split())) # Collection da ocorrência das palavras no texto. 

print("----------------------------------------------------------------------------------------------------")

print((Counter(a_lenda_da_serpente.split())).most_common(10)) # Collection das 10 palavras mais comuns do texto.

print("----------------------------------------------------------------------------------------------------")
