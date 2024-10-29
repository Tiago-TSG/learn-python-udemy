print("----------------------------------------------------------------------------------------------------")

def diz_oi():
    return("Oi, ")

alguem = "Evelyn"

print(f"{diz_oi() + alguem}!")

print("----------------------------------------------------------------------------------------------------")

def diz_oi_com_print_depois():
    return("Olá, Mundo!")
    print("Print após o retorno...") # OBS: A palavra reservada return finaliza a função, por isso, tudo depois dela não será executado.

print(diz_oi_com_print_depois())

print("----------------------------------------------------------------------------------------------------")

def diz_oi_com_print_antes():
    print("Print após o retorno...") # OBS: Neste caso, o print será exibido, pois aparece antes do "return" na função.
    return("Olá, Mundo!")
    
print(diz_oi_com_print_antes())

print("----------------------------------------------------------------------------------------------------")
