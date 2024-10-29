print("----------------------------------------------------------------------------------------------------")

def data():

    data = input(f"Digite a data atual (dd/mm/year): ")
    lista = data.split("/")

    dia = int(lista[0])
    mes = int(lista[1])
    ano = int(lista[2])

    if mes == 1:
        mes_str = "Janeiro"
    
    elif mes == 2:
        mes_str = "Fevereiro"

    elif mes == 3:
        mes_str = "Março"

    elif mes == 4:
        mes_str = "Abril"

    elif mes == 5:
        mes_str = "Maio"

    elif mes == 6:
        mes_str = "Junho"

    elif mes == 7:
        mes_str = "Julho"

    elif mes == 8:
        mes_str = "Agosto"

    elif mes == 9:
        mes_str = "Setembro"

    elif mes == 10:
        mes_str = "Outubro"

    elif mes == 11:
        mes_str = "Novembro"

    elif mes == 12:
        mes_str = "Dezembro"

    else:
        mes_str = "Mês desconhecido"
    print("----------------------------------------------------------------------------------------------------")
    return(f"Hoje é dia {dia} de {mes_str} de {ano}.")

print(data())

print("----------------------------------------------------------------------------------------------------")
