# Leia estoque (int) e vendidas (int). Atualize com -= e mostre o estoque final.

print ("Digite o estoque: ")
estoque = int(input())
print ("Digite o número de unidades vendidas: ")
vendidas = int(input())
estoque -= vendidas
print ("O estoque final é: ", estoque)
