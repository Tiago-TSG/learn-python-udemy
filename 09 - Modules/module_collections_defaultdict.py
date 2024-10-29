from collections import defaultdict

print("----------------------------------------------------------------------------------------------------")

time = {"time": "Vasco da Gama"}

print(time)
print(time["time"])

print("----------------------------------------------------------------------------------------------------")

# print(time["time2"]) # Forçando o "KeyError" (Comentado para não parar a execução do código)

print("----------------------------------------------------------------------------------------------------")

time_outro = defaultdict(lambda: "")

time_outro["time-1"] = "Vasco da Gama"
time_outro["time-2"] = "Palmeiras"

print(time_outro["time-3"]) # Utilizando o modulo defaultdict, o "keyError" não é exibido e a chave é adicionada na variável, contendo o valor default. 
print(time_outro)

print("----------------------------------------------------------------------------------------------------")
