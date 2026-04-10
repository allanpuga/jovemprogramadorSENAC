# Leia estoque (int). Subtraia venda com -=, depois reposição com +=, por fim %= 6.
# Solicite um valor de estoque (int), subtraia as vendas utilizando -= e depois a reposição do estoque utilizando +=, por fim, aplique %= 6. 

print ("Digite o estoque: ")
estoque = int(input())
print ("Digite o número de unidades vendidas: ")
vendidas = int(input())
estoque -= vendidas
print ("Digite o número de unidades repostas: ")
reposicao = int(input())
estoque += reposicao
estoque %= 6
print ("O estoque final é: ", estoque)

