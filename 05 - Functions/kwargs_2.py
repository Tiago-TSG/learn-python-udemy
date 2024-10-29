"""
Ordem de declaração nas funções:

- Parâmetros obrigatórios
- *args
- Parâmetros default
- **kwargs

"""

print("----------------------------------------------------------------------------------------------------")

def formulario(nome, idade, sexo, cor, *args, estado_civil = "solteiro", **kwargs): # OBS.: FORMA NA ORDEM CORRETA DOS PARÂMETROS
    print(f"O candidato {nome.title()} tem {idade} anos e a cor dele é {cor}.")
    print(f"Sexo = {sexo}")
    print(f"Estado Civil = {estado_civil}")
    if "profissão" in kwargs:
        print(f"Profissão = {kwargs['profissão']}")
    print(args)

formulario("tiago", 40, "masculino", "branca", 4, 6, 7, profissão = "SRE | Devops")

print("----------------------------------------------------------------------------------------------------")

def formulario_2(nome, idade, sexo, cor, estado_civil = "solteiro", *args, **kwargs): # OBS.: FORMA NA ORDEM CORRETA DOS PARÂMETROS
    print(f"O candidato {nome.title()} tem {idade} anos e a cor dele é {cor}.")
    print(f"Sexo = {sexo}")
    print(f"Estado Civil = {estado_civil}")
    if "profissão" in kwargs:
        print(f"Profissão = {kwargs['profissão']}")
    print(args)

formulario_2("tiago", 40, "masculino", "branca", 4, 6, 7, profissão = "SRE | Devops")

print("----------------------------------------------------------------------------------------------------")
