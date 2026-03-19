# Atualizar preço e quantidade; calcular o total Tarefa: Leia produto = {"nome": str, "preco": float, "quantidade": int}. Aplique aumento percentual ao preço e some 2 unidades na quantidade. Calcule total = preco * quantidade e exiba.Use: float(), int(), input(), acesso/atribuição por chave, print()Tipos: str, float, int, dict.Conceitos: operadores aritméticos (*, +), atualização de valores no dict.

produto = {}
produto["nome"] = input("Digite o nome do produto: ")
produto["preco"] = float(input("Digite o preço do produto: "))
produto["quantidade"] = int(input("Digite a quantidade do produto: "))
aumento_percentual = float(input("Digite o aumento percentual (ex: 10 para 10%): "))
# Atualizar preço com aumento percentual
produto["preco"] += produto["preco"] * (aumento_percentual / 100)
# Atualizar quantidade somando 2 unidades
produto["quantidade"] += 2
# Calcular total
total = produto["preco"] * produto["quantidade"]
print(f"Produto: {produto['nome']}")
print(f"Preço atualizado: {produto['preco']:.2f}")
print(f"Quantidade atualizada: {produto['quantidade']}")
print(f"Total: {total:.2f}")

