# Formato de função : funçao()
# Formato de método : objeto.função() # Obs.: Também é uma função, porém associada a um objeto.

def dar_oi():  # Sempre com letras minúsculas e caso seja um novo composto, sempre separado por "_".
    return  ("Oi!")

if __name__ == "__main__":
    
    print("----------------------------------------------------------------------------------------------------")

    print(dar_oi())

    print("----------------------------------------------------------------------------------------------------")
    
    def cantar_parabens():
        print("Parabéns pra você, nesta data querida. Muitas felicidades e muitos anos de vida!")

    cantar_parabens()

    print("----------------------------------------------------------------------------------------------------")

    canta = cantar_parabens # NÃO RECOMENDADO!
    canta()

    print("----------------------------------------------------------------------------------------------------")

    for i in range(5):
        cantar_parabens()

    print("----------------------------------------------------------------------------------------------------")
