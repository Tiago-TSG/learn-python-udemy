from random import random # A função random gera um pseudo-randômico entre "0" e "1".

print("----------------------------------------------------------------------------------------------------")

def joga_moeda():
    if random() < 0.5:
        return("Cara")
    else:
        return("Coroa")
    
print(joga_moeda())

print("----------------------------------------------------------------------------------------------------")

def num_par_ou_impar():
    numero = 4
    if numero % 2 != 0:
        return(f"O número {numero} é ímpar.")
    else:
        return(f"O número {numero} é par.")

print(num_par_ou_impar())

print("----------------------------------------------------------------------------------------------------")
