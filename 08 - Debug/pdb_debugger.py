# Para utilizar a biblioteca do PDB e degugar o código é necessário importá-la.

###################
# COMANDOS DO PDB # 
###################

# l (lista onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução / finaliza o debbuging)

import pdb 

print("----------------------------------------------------------------------------------------------------")

nome = 'Angelina'
sobrenome = 'jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Python Essencial'
final = nome_completo + 'faz o curso' + curso

print(final)

print("----------------------------------------------------------------------------------------------------")

# Outra forma de fazer, caso a biblioteca não tivesse sido importada.
# OBS.: Geralmente é utilizado para não termos que alterar as bibliotecas importadas no início do código,
# já que, o pdb só será utilizado para o deg do código e retirado posteriormente.

nome = 'Angelina'
sobrenome = 'jolie'
import pdb; pdb.set_trace() # Dois comandos separados por ';' podem ser executados na mesma linha no Python.
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Python Essencial'
final = nome_completo + 'faz o curso' + curso

print(final)

print("----------------------------------------------------------------------------------------------------")

# OBS.: A partir do Python 3.7 (a versão utilizada aqui já é mais avançada 3.8), não é mais necessária a importação das bibliotecas PDB.
# A função do debbuger passou a ser built-in (integrada). Passou a ser chamada de breakpoint()

nome = 'Angelina'
sobrenome = 'jolie'
breakpoint() # Nova função integrada, que faz o debbuger do código. Os comandos são os mesmos do PDB.
nome_completo = nome + ' ' + sobrenome
curso = 'Programação Python Essencial'
final = nome_completo + 'faz o curso' + curso

print(final)

print("----------------------------------------------------------------------------------------------------")

# OBS.: Ficar atendo com o conflito entre variáveis e os comandos do PDB / BreakPoint.
# Caso alguma variável seja igual a um comando (ex: 'l'), é necessário imprimir com o comando 'p' (p nome_variavel).
# Neste caso, seria "p l" .
# O recomendado é sempre nomear as variáveis com nomes que tenham algum significado, para evitar esse tipo de problema.
