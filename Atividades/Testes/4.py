# Escreva uma função get_sign que receba um número inteiro number como entrada e retorne o sinal do número fornecido como uma string.
# Requisitos
# O inteiro de entrada number pode ser qualquer inteiro dentro do intervalo do tipo int do Python.
# A função deve retornar "Positive" se o number de entrada for positivo (maior que 0), "Negative" se for negativo (menor que 0) e "Zero" se for igual a 0.
# A função não deve modificar o number de entrada.

print("Atividade 4: Obter o sinal do número")
def get_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
# Testando a função com diferentes números
test_numbers = [10, -5, 0]
for num in test_numbers:
    print(f"O sinal de {num} é: {get_sign(num)}")
    