# Inicie fila = ["Ana", "Bruno"]. Imprima a fila.

fila = ["Ana", "Bruno"]
print(f"Fila inicial: {fila}")
# Ler dois nomes e adicionar à fila
nomes = input("Digite dois nomes separados por vírgula: ").split(",")
fila.extend(nomes)
print(f"Fila após adicionar nomes: {fila}")
# Ler cliente prioritário e inserir na posição 1 se o cliente prioritário não for vazio se tiver na lista alterar a ordem para o cliente prioritário ficar na posição 1

cliente_prioritario = input("Digite o nome do cliente prioritário: ")
if cliente_prioritario:
    if cliente_prioritario in fila:
        fila.remove(cliente_prioritario)
    fila.insert(1, cliente_prioritario)
    print(f"Fila após inserir cliente prioritário: {fila}")
# Atender o primeiro cliente
cliente_atendido = fila.pop(0)
print(f"Cliente atendido: {cliente_atendido}")
print(f"Fila final: {fila}")


