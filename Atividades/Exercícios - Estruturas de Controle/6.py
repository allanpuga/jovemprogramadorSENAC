# Faça uma calculadora simples contendo as operações: soma, subtração, divisão e multiplicação. Solicite ao usuário que informe dois número e que informe também a operação que deseja realizar (+, -, /, *) e depois exiba o resultado.
numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
operacao = input("Informe a operação que deseja realizar (+, -, /, *): ")

if operacao == "+":
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "/":
    resultado = numero1 / numero2
    print(f"O resultado da divisão é: {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
else:
    print("Operação inválida.")

