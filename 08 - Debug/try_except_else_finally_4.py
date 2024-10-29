# OBS.: Outra forma correta e enxuta de se fazer a tratativa de erros.

print("----------------------------------------------------------------------------------------------------")

def divisao(a, b):
    print(f"a={a} b={b}") # OBS.: Trecho de código necessário caso se deseje saber quais valores a função está recebendo.
    print("----------------------------------------------------------------------------------------------------")
    try:
        return(int(a) / int(b))
    
    except (ValueError, ZeroDivisionError) as err:
        return(f"Ocorreu um problema: {err}")
    
num_1 = input("Digite o primeiro número: ")
num_2 = input("Digite o primeiro número: ")

print("----------------------------------------------------------------------------------------------------")

print(f" Adivisão de '{num_1}' por '{num_2}' é: '{divisao(num_1, num_2)}'.")

print("----------------------------------------------------------------------------------------------------")
