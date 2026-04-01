# Utilizar while para: Solicitar o valor de uma compra, Somar os valores informados, Continuar pedindo valores até o usuário digitar 0. Ao final, mostrar: Total das compras, Quantidade de compras realizadas, Valor médio das compras.

total_compras = 0
quantidade_compras = 0

while True:
 
    valor_compra = float(input(f"Informe o valor da compra {quantidade_compras + 1}° (ou 0 para sair): R$ "))
    if valor_compra == 0:
        break
    total_compras += valor_compra
    quantidade_compras += 1

if quantidade_compras > 0:
    valor_medio = total_compras / quantidade_compras
else:
    valor_medio = 0

print(f"Total das compras: R$ {total_compras:.2f}")
print(f"Quantidade de compras realizadas: {quantidade_compras}")
print(f"Valor médio das compras: R$ {valor_medio:.2f}")
