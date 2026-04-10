def soma(a, b, c):
    soma = a + b + c
    return soma 

def media(a, b, c):
    media = (a + b + c) / 3
    return media

print(media(1, 2, 3))

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: ")) 
c = int(input("Digite o terceiro número: "))

print("A soma dos números é: ", soma(a, b, c))
print("A média dos números é: ", media(a, b, c))

