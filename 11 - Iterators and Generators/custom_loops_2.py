# Criando seu for customizado

def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for(range(1, 11))

print("----------------------------------------------------------------------------------------------------")

meu_for("Vasco da Gama")

print("----------------------------------------------------------------------------------------------------")


# Outro exemplo, utilizando uma "class"

class Contador():
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        else:
            raise StopIteration
       
con = Contador(1, 61)

print(next(con))
print(next(con))
print(next(con))

print("----------------------------------------------------------------------------------------------------")

con = meu_for(Contador(1, 61)) # Obs.: Desse jeito, a função "meu_for" imprime "none" para o "StopIteration".

print(con)

print("----------------------------------------------------------------------------------------------------")

for num in Contador(1, 61): # Com esse "for" iterando no "Contador", os números são impressos corretamente.
    print(num)

print("----------------------------------------------------------------------------------------------------")
