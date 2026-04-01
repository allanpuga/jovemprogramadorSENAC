# Solicite ao usuário que informe um número e depois exiba se o número é positivo, negativo ou zero.
numero = float(input("Informe um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
