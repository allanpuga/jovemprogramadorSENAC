# Organizar valores sem mexer na tupla original
# Tarefa: Leia quatro números em uma tupla e exiba: 
# a tupla original
# uma lista ordenada apenas para visualização
# o tipo da variável ordenada
# Objetivo: mostrar diferença entre tupla e lista sem precisar modificar nada.Use: sorted(), print(), type()

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
tupla_numeros = (num1, num2, num3, num4)
print(f"Tupla original: {tupla_numeros}")
lista_ordenada = sorted(tupla_numeros)
print(f"Lista ordenada: {lista_ordenada}")
print(f"Tipo da variável ordenada: {type(lista_ordenada)}")

