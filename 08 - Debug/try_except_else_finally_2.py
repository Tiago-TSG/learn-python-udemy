# OBS.: Forma incorreta de se tratar errps de uma função (eles devem ser tratados dentro da função.)

print("----------------------------------------------------------------------------------------------------")

def divisao(a, b):
    return(a / b)

try: 
    num_1 = int(input("Digite o primeiro número: "))

except ValueError:
    print(" O Valor precisa ser numérico.")

try:   
    num_2 = int(input("Digite o segundo número: "))

except:
    print(" O Valor precisa ser numérico.")

try:
    print(divisao(num_1, num_2))

except NameError:
    print("Valor incorreto.")

print("----------------------------------------------------------------------------------------------------")
