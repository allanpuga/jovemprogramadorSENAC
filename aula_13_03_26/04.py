# Leia estoque (int) e vendidas (int). Atualize com -= e mostre o estoque final.
# Solicite ao usuário que informe o estoque no início do dia (int) e a quantidade vendida ao final do dia (int). Atualize a quantidade utilizando atribuição -= para mostrar o estoque final.  


print ("Digite o estoque: ")
estoque = int(input())
print ("Digite o número de unidades vendidas: ")
vendidas = int(input())
estoque -= vendidas
print ("O estoque final é: ", estoque)
