produto = ""
carrinho = [""]

while produto != "pagamento":
    print("Digite o nome de uma produto ou digite pagamento para continuar para etapa de pagamento: ")
    produto = input()
    if produto != "pagamento":
        carrinho.append(produto)
for produto in carrinho:
    print(produto)
    print ("--------------------------")
