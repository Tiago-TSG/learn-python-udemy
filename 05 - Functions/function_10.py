print("----------------------------------------------------------------------------------------------------")

professora = "Augusta" # Variável global pode ser chamada por qualquer bloco de programação.
print(f"Oi, professora {professora}!")

def oi_professora():
    """ Função que retorna uma saudação a professora Evelyn. """ # Para documentar um função, devemos utilizar as aspas.
    professora = "Evelyn" # Uma variável local sobreepôem uma variável global e não pode ser chamada fora do bloco de progração que ela foi criada.
    return(f"Oi, professora {professora}!")

print(oi_professora())

def oi_professora_2():
    return(f"Oi, professora {professora}!")

print(oi_professora_2()) # OBS.:Como a variável não foi inicializada dentro da função, ela chamará a variável global "professora".

print("----------------------------------------------------------------------------------------------------")

professora = "Evelyn"

def oi_professora_3():
    global professora # Citando que queremos utilizar a variável global "professora".
    return(f"Oi, professora {professora}!")

print(oi_professora_3())

print("----------------------------------------------------------------------------------------------------")

def fora():
    contador = 0

    def dentro(): # Função dentro de outra
        nonlocal contador

        contador = contador + 10
        return(contador)
    return(dentro())
    
print(fora()) # OBS.: É preciso chamar a função mais externa para obter o resultado da função interna.

print("----------------------------------------------------------------------------------------------------")
