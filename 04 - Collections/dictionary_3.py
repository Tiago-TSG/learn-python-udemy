print("----------------------------------------------------------------------------------------------------")

receita = dict(jan = "R$100,00", fev = "R$350,00", março = "R$750,00", abril = "R$1020,00")
print(receita)

receita["maio"] = "R$1500,00" # Forma de atualização ou adição de novos dados em um dicionário, mais comum.
print(receita)

print("----------------------------------------------------------------------------------------------------")

novo_dado = dict(junho = "R$2300,00")

receita.update(novo_dado)
print(receita)

novo_dado_2 = {"julho": "R$3200,00"}

receita.update(novo_dado_2)
print(receita)

novo_dado_3 = dict(fev = "R$430,00")

receita.update(novo_dado_3)
print(receita)

receita["maio"] = "R$1600,00"
print(receita)

print("----------------------------------------------------------------------------------------------------")
