# Leia um número (int), aplique n %= 2 e imprima.
# Solicite um número (int), aplique n %= 2 e exiba o valor na tela. Se o resultado for 0, o número é par; se o resultado for 1, o número é ímpar. 
# Se o resultado for 0 = print par, se o resultado for 1 = print ímpar

n = int(input("Digite um número: "))

n %= 2

if n == 0:
    print("O numero é par)")
else:
    print("O numero é Ímpar")

    