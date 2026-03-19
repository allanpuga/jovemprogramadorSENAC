# Exibir maior e menor valor
# Tarefa: Leia quatro números inteiros, coloque em uma tupla e exiba o maior e o menor.
# Orientações: 
# funções: max(), min()
# tipos: int, tuple
# conceito: operações básicas de agregação

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
tupla_numeros = (num1, num2, num3, num4)
print(f"O maior número é: {max(tupla_numeros)}")
print(f"O menor número é: {min(tupla_numeros)}")

