print("----------------------------------------------------------------------------------------------------")

# OBS.: O "strip" retira os espaços no início e final da string (não retira espaços no meio) e o "title" transforma a primeira letra das strings em maiúsculas.

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()  


print(nome_completo("tiago", "da silva gonçalves       "))
print(nome_completo("evelyn   ", "dos santos lisbôa    "))

print("----------------------------------------------------------------------------------------------------")

# lambda x1, x2, x3, ... xn: [expressão]

time = lambda: "Vasco da Gama"

lambda_uma_entrada = lambda x: x * 3 + 1

lambda_duas_entradas = lambda x, y: x * y + 10 

lambda_tres_entradas = lambda x, y, z: (x * y + 10) / z


print(time())

print(lambda_uma_entrada(5))

print(lambda_duas_entradas(6, 8))

print(lambda_tres_entradas(3, 7, 4))

print("----------------------------------------------------------------------------------------------------")
