print("----------------------------------------------------------------------------------------------------")

def cores_favoritas(**kwargs): # OBS.: O **Kwargs trabalha com dicionários.
    for pessoa, cor in kwargs.items():
        print(f"A cor favorita da {pessoa.title()} é {cor}.")

cores_favoritas(tiago =  "azul", evelyn = "roxo", luiza = "rosa", daniel = "laranja")

cores_favoritas(ernesto = "verde")

print("----------------------------------------------------------------------------------------------------")


def ola_tia(**kwargs):
    if "evelyn" in kwargs and kwargs["evelyn"] == "inglês":
        return ("Teremos aula com a tia Evelyn!")
    else:
        return("Poxa, não teremos aula com a tia Evelyn...")

print(ola_tia(tiago = "música", evelyn = "inglês"))

print("----------------------------------------------------------------------------------------------------")

def professor_materia(**kwargs):
    for professor, materia in kwargs.items():
        print(f"Teremos aulas de {materia} com o/a professor/a {professor.title()}.")

professor_materia(tiago = "música", evelyn = "inglês")

print("----------------------------------------------------------------------------------------------------")
