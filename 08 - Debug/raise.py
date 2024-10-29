# O raise não é uma função e sim uma palavra reservada que permite criar exceções personalizadas no código.
# O raise, assim como o return, finaliza uma função.

print("----------------------------------------------------------------------------------------------------")

def colore(texto, cor):
    if type(texto) != str:
        raise TypeError("O Texto precisa ser uma string")
    if type(cor) != str:
        raise TypeError("A cor precisa ser uma string")
    print(f" O texto '{texto}' será impresso com a cor {cor}.")

# colore(3,"preto") # Para testar o raise

# colore("Vasco", 4) # Para testar o raise

colore("Vasco", "Preto")

print("----------------------------------------------------------------------------------------------------")

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) != str:
        raise TypeError("O Texto precisa ser uma string")
    
    if type(cor) != str:
        raise TypeError("A cor precisa ser uma string")
    print(f" O texto '{texto}' será impresso com a cor {cor}.")
    
    if cor not in cores:
        raise ValueError(f"A cor precisa estar contida em {cores}.")
    
    print("Print no final da função.") # Executa somente se não der match em algum dos raises declarados.
    
colore("Vasco", "branco")

print("----------------------------------------------------------------------------------------------------")

colore("Vasco", "preto") # Forçando a utilização do raise.

print("----------------------------------------------------------------------------------------------------")
