# OBS.:Tratar os erros de forma genérica, não é a melhor forma de se tratar erros. O ideal é tratar sempre de forma específica.
# Continuação...

try:
    len(5)
except TypeError as err:
    print("----------------------------------------------------------------------------------------------------")
    print(f"Essa aplicação gerou o seguinte erro: '{err}.'")  # Essa aplicação gerou o seguinte erro: 'object of type 'int' has no len().'
    print("----------------------------------------------------------------------------------------------------")


try:
    len(5)
except NameError as err_a:
    print(f"Essa aplicação gerou um 'NameError': {err_a}.")
    print("----------------------------------------------------------------------------------------------------")

except TypeError as err_b: 
    print(f"Essa aplicação gerou um 'TypeError': {err_b}.") # Essa aplicação gerou um 'TypeError': object of type 'int' has no len().
    print("----------------------------------------------------------------------------------------------------")


try:
    len('Vasco'[5])
except NameError as err_a:
    print(f"Essa aplicação gerou um 'NameError': {err_a}.")
    print("----------------------------------------------------------------------------------------------------")

except TypeError as err_b: 
    print(f"Essa aplicação gerou um 'TypeError': {err_b}.") # Essa aplicação gerou um 'TypeError': object of type 'int' has no len().
    print("----------------------------------------------------------------------------------------------------")

except:
    print(f"Essa aplicação gerou um erro não esperado.")
    print("----------------------------------------------------------------------------------------------------")


def pega_valor(dicionario, chave):
    try:
        return(dicionario[chave])
    except KeyError:
        return None
    except TypeError:
        return None
        
    
dicionario_1 = {"time": "Vasco"}

print(pega_valor(dicionario_1, "time")) # Vasco

print("----------------------------------------------------------------------------------------------------")

print(pega_valor(dicionario_1, "teste")) # None

print(pega_valor(8, "Vasco")) # None

print("----------------------------------------------------------------------------------------------------")
