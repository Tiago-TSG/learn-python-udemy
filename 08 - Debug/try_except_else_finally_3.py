# OBS.: Forma correta de se tratar erros (Eles devem ser tratados dentro da função.)

print("----------------------------------------------------------------------------------------------------")

def divisao(a, b):
    try:
        return(int(a) / int(b))
    
    except ValueError:
        return("Valores incorretos. Por favor, digite dois números inteiros.")
    
    except ZeroDivisionError:
        return("Não é possível dividir um número por '0'.")

num_1 = input("Digite o primeiro número: ")
num_2 = input("Digite o primeiro número: ")

print("----------------------------------------------------------------------------------------------------")

print(f" Adivisão de '{num_1}' por '{num_2}' é: '{divisao(num_1, num_2)}'.")

print("----------------------------------------------------------------------------------------------------")
