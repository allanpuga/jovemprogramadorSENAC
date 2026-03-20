data = [
    {"id":1, "nome": "Maria", "salario": 4500.03},
    {"id":2, "nome": "José", "salario": 6500.05},
    {"id":3, "nome": "Antonio", "salario": 3409.98},
    {"id":4, "nome": "Ana", "salario": 5093.34},
    {"id":5, "nome": "Mariana", "salario": 3458.54},
    {"id":6, "nome": "Ana", "salario": 10932.59},
]
print(data)

# Média de salário
#Qual o valor do salário médio?
total_salarios = sum(item["salario"] for item in data)
media_salarios = total_salarios / len(data)
print(f"A média dos salários é: {media_salarios:.2f}")

# Quantidade de Linhas
# Qual a quantidade de linhas do DataFrame
quantidade_linhas = len(data)
print(f"A quantidade de linhas do DataFrame é: {quantidade_linhas}")

# Quantidade de colunas
# Qual a quantidade de colunas do DataFrame
quantidade_colunas = len(data[0]) if data else 0
print(f"A quantidade de colunas do DataFrame é: {quantidade_colunas}")

# Estatísticas Descritivas
#Calcule as principais estatísticas descritivas do salário: mínimo, 1o quartil, média, mediana, 3o quartíl, máximo e desvio padrão.
salarios = [item["salario"] for item in data]
min_salario = min(salarios)
max_salario = max(salarios)
media_salario = sum(salarios) / len(salarios)
salarios_ordenados = sorted(salarios)
mediana_salario = salarios_ordenados[len(salarios) // 2] if len(salarios) % 2 != 0 else (salarios_ordenados[len(salarios) // 2 - 1] + salarios_ordenados[len(salarios) // 2]) / 2
desvio_padrao_salario = (sum((x - media_salario) ** 2 for x in salarios) / len(salarios)) ** 0.5
print(f"Salário mínimo: {min_salario:.2f}")
print(f"Salário máximo: {max_salario:.2f}")
print(f"Salário médio: {media_salario:.2f}")
print(f"Mediana dos salários: {mediana_salario:.2f}")
print(f"Desvio padrão dos salários: {desvio_padrao_salario:.2f}")
