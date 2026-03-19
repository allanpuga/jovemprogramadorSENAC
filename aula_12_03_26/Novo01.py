# Crie uma lista vazia​, tilize print() para exibir a lista de compras a cada adição ou remoção de um item da lista, Utilize append() para adicionar itens à lista, Utilize remove() para remover itens da lista

lista_compras = []
print("Lista de compras: ", lista_compras)
print("Digite um item para adicionar à lista de compras: ")
item = input()
lista_compras.append(item)
print("Lista de compras: ", lista_compras)
print("Digite um item para remover da lista de compras: ")
item = input()
lista_compras.remove(item)
print("Lista de compras: ", lista_compras)
