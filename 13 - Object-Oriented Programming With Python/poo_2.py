# Programação orientada à objetos (POO)

"""

- Classe -> Modelo de um objeto do mundo real, sendo representado computacionalmente.


Obs.: Quando criamos sistemas e precisamos definir quais classes necessitaremos, os objetos que serão mapeados para classes são chamados de "entidades".

Obs.: Não se deve utilizar caracteres especiais ou acentuações em programação. 
E para o caso das classes criadas, sempre utilizar "CamelCase" em seu formato. 

Obs.: Classes internas do Python possuem letras minúsculas em seus nomes, por convenção.


"""

# Classes (Imagine que você queira criar um sistema para automatizar a ligação de lâmpadas de uma casa.)

class Lampada(): # Obs.: Por convenção, deve-se começar todo nome de classe criada com letra maiúscula (incluindo nomes compostos. ex: ContaCorrente)
    pass # Palavra reservada utilizada quando ainda não definimos as configurações de um bloco em Python.

lamp = Lampada()
print(type(lamp))

# Outro formato de nome de classe, utilizando "CamelCase".

class ContaCorrente(): 
    pass

# Atributos
# No caso de uma lâmpada, poderiam ser:

""" 
- cor
- luminosidade
- potência

etc...

"""

# Métodos
# No caso de um sistema para controlar lâmpadas, poderiam ser:

""" 
- ligar
- desligar

etc...

"""
