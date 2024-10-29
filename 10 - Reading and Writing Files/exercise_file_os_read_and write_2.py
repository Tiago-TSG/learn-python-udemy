# Programa que verifica o número de vogais e consoantes de um texto em um arquivo informado pelo usuário.

# Código inicial com problemas (TRANSVERSAL PATH), quando o usuário pode colocar qualquer path na busca (ex: /etc/passwd).
# Foi necessário fazer da seguinte maneira:

import os

# Solicita o nome do arquivo ao usuário
nome_arquivo = input("Digite o nome de um arquivo para análise: ")

# Define o diretório permitido
diretorio_permitido = os.path.normpath(os.path.abspath("/home/tiago/estudos/python/geek-university/10 - Reading and Writing Files"))

try:
    # Constrói o caminho completo do arquivo
    caminho_arquivo = os.path.normpath(os.path.join(diretorio_permitido, nome_arquivo))

    # Verifica se o caminho do arquivo está dentro do diretório permitido
    if not caminho_arquivo.startswith(diretorio_permitido):
        raise ValueError("Acesso não autorizado. (Attempted path traversal)")
    
    # Se a checagem do path for segura, proceder com a análise do arquivo
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()

except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o nome e tente novamente.")
except Exception as Error:
        print(f"Ocorreu um erro ao abrir o arquivo: {Error}")

else:
    vogais = 0
    consoantes = 0

    for linha in linhas:
        linha = linha.replace("\n", "").lower()
        for caractere in linha:
            if caractere in ['a', 'e', 'i', 'o', 'u']:
                vogais += 1
            elif caractere.isalpha():
                consoantes += 1

    print("----------------------------------------------------------------------------------------------------")

if vogais > 0:
        print(f"Existe(m) {vogais} vogais no texto.")
else:
    print("Não existem vogais no texto.")

if consoantes > 0:
    print(f"Existe(m) {consoantes} consoantes no texto.")
else:
    print("Não existem consoantes no texto.")
            
print("----------------------------------------------------------------------------------------------------")
