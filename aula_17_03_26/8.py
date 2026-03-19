# Remover uma chave com segurança. Tarefa: Leia produto = {"nome": str, "preco": float}. Tente remover a chave "desconto" se existir, sem gerar erro. Mostre antes e depois.  Use: input(), float(), dict.pop("chave", valor_padrao), print() Tipos: str, float, dict. Conceitos: remoção segura, estado antes/depois.

produto = {}
produto["nome"] = input("Digite o nome do produto: ")
produto["preco"] = float(input("Digite o preço do produto: "))
print("Antes:", produto)
# O segundo argumento no pop evita o erro se a chave não existir
produto.pop("desconto", None)
print("Depois:", produto)

