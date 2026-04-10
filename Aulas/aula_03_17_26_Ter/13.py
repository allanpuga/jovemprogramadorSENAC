# Contar quantas vezes um número aparece
# Tarefa: Leia quatro números inteiros e crie uma tupla. Depois leia um número e diga quantas vezes ele aparece na tupla.
#Orientações: 
#método: tuple.count()
# tipos: int, tuple

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
tupla_numeros = (num1, num2, num3, num4)
numero_verificar = int(input("Digite um número para verificar quantas vezes aparece na tupla: "))
contador = tupla_numeros.count(numero_verificar)
print(f"O número {numero_verificar} aparece {contador} vezes na tupla.")

