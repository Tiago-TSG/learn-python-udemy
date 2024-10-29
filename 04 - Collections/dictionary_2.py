paises = dict(ar= "Argentina", eua= "Estados Unidos", jp= "Japão", bg= "Bulgária", cu= "Cuba", it= "Itália")

pais = paises.get("ru")

print("----------------------------------------------------------------------------------------------------")

if pais:
    print(f"Encontrei o país {pais}")
else:
    print("Não encontrei o país")

print("----------------------------------------------------------------------------------------------------")

pais = paises.get("ru", "Não encontrei o país") # Se não encontrar o país, o valor torna-se o segumento campo ("Não encontrei o país"), não precisando mais do "IF".

print(pais)

print("----------------------------------------------------------------------------------------------------")

print("br" in paises) # Como não existe a chave "br", retorna o valor "False".
print("jp" in paises) # Como existe a chave "jp", retorna o valor "True"
print("Estados Unidos" in paises) # Não traz o valor e sim a chave. Por isso, é falso.

print("----------------------------------------------------------------------------------------------------")


sigla = input(" Digite a sigla de um país: ")

print("----------------------------------------------------------------------------------------------------")

if sigla in (paises):
    p = paises.get(sigla)
    print(f"O país '{p}', foi encontrado.")
else:
    print("Nenhum país com esta sigla, foi encontrado.")

print("----------------------------------------------------------------------------------------------------")
