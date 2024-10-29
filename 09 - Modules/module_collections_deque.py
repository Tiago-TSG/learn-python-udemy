from collections import deque

print("----------------------------------------------------------------------------------------------------")

palavra = "Vasco"

palavra_letras = list(palavra)
print(palavra_letras)

palavra_letras.append(" ")
palavra_letras.append("da")
palavra_letras.append(" ")
palavra_letras.append("Gama ")

print(palavra_letras)

print("----------------------------------------------------------------------------------------------------")

palavra = "Vasco"

palavra_letras = list(palavra)
print(palavra_letras)

palavra_letras.extend(" da Gama")
print(palavra_letras)

print("----------------------------------------------------------------------------------------------------")

palavra_deque = deque(palavra)
print(palavra_deque)

palavra_deque.extend(" da Gama")
print(palavra_deque)

palavra_deque.appendleft("Time:") # Possibilidade de adicionar um item mais a esquerda com o método "deque".
print(palavra_deque)

print(palavra_deque.popleft()) # Possibilidade de remoção do item mais a esquerda com o método "deque".
print(palavra_deque)

palavra_deque.extendleft(reversed("Time: ")) # Foi necessário o reversed para colocar a string "Time: " na posição correta.
print(palavra_deque) # Possibilidade adicionar mais de um item a esquerda com o método "deque".

print("----------------------------------------------------------------------------------------------------")
