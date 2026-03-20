# Máximo de Três
# Escreva uma função max_of_three que receba três inteiros a, b e c como entrada e retorne o máximo dos três números fornecidos.
#Requisitos
# Os inteiros de entrada a, b e c podem ser qualquer inteiro dentro do intervalo do tipo int do Python.
# A função deve retornar o máximo dos três números de entrada.
# A função não deve modificar os números de entrada.

print("Atividade 5: Máximo de três números")
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
# Testando a função com diferentes conjuntos de números
test_cases = [(3, 5, 2), (10, 7, 15), (-1, -5, -3), (0, 0, 0)]
for a, b, c in test_cases:
    print(f"O máximo de {a}, {b} e {c} é: {max_of_three(a, b, c)}") 

    