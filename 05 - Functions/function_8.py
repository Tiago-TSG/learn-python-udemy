print("----------------------------------------------------------------------------------------------------")

def exponencial(numero, potencia = 2):
    return (numero ** potencia)

print(exponencial(4, 3)) # OBS.: Os valores informados para o parâmetro "potencia", irão substituir o valor padrão.
print(exponencial(2, 3))
print(exponencial(5, 6))
print(exponencial(4)) # OBS.: Como foi informado um valor default para o segundo parâmetro da função (potencia), caso não informado e usará o "2".

print("----------------------------------------------------------------------------------------------------")

def ola_professora(nome = "Evelyn", professora = True):
    if nome == "Evelyn" and professora == True:
        return("Bem-vinda, professora Evelyn!")
    elif nome == "Evelyn" and professora == False:
        return(f"Eu pensei que você era a professora Evelyn!")
    else:
        return(f"Olá, {nome}!")
    
print(ola_professora())
print(ola_professora("Tiago"))
print(ola_professora("Evelyn", False))

print("----------------------------------------------------------------------------------------------------")
