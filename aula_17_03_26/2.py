# 1. Leia quatro inteiros e crie uma lista
print ('Digite quatro números inteiros para criar uma lista:')
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
lista = [n1, n2, n3, n4]
print("Lista criada:", lista)

# Leia um valor alvo e remova se ele estiver na lista.
alvo = int(input("Digite um valor alvo para remover da lista: "))

# 3. Mostre o tamanho antes
print("Tamanho da lista antes de remover o alvo:", len(lista))

# 4. Remova se ele estiver na lista (teste de pertencimento)
if alvo in lista:
    lista.remove(alvo)
    print(f"Valor {alvo} removido da lista.")
else:
    print(f"Valor {alvo} não encontrado na lista.")

# 5. Mostre o tamanho depois
print("Tamanho da lista depois de remover o alvo:", len(lista)) 
print("Lista final:", lista)

