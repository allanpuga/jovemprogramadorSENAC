# Escreva uma função is_positive que receba um número inteiro number como entrada e retorne True se o número fornecido for positivo e False caso contrário.
# Requisitos
# O inteiro de entrada number pode ser qualquer inteiro dentro do intervalo do tipo int do Python.
# A função deve retornar True se o number de entrada for positivo (maior que 0) e False caso contrário.
# A função não deve modificar o number de entrada.
# Tente usar uma estrutura condicional 'if/else' ou uma expressão de comparação para atingir o objetivo solicitado
# Complete a função garantindo que ela retorne 'True' para números maiores que 0 e 'False' nos outros casos.

print("Atividade 3: Verificar se o número é positivo")
number = int(input("Digite um número inteiro: "))
def is_positive(number):
    if number > 0:
        return True
    else:
        return False
    