# Crie uma função que receba dois números e retorne a soma deles. 

def soma(a, b):
    soma = a + b
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: ")) 
    return soma

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
result = soma(a, b) 
print("A soma dos números é: ", result)
