# Nova atividade de testes para o curso de Python
# Esta atividade tem como objetivo praticar a criação de funções e o uso de estruturas de controle de fluxo
# Escreva uma função chamada "verificar_numero" que recebe um número como parâmetro e retorna:
# - "Positivo" se o número for maior que zero
# - "Negativo" se o número for menor que zero
# - "Zero" se o número for igual a zero
print("Atividade 1: Verificar número")
numero = float(input("Digite um número: "))
def verificar_numero(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Zero"
resultado = verificar_numero(numero)
print(f"O número {numero} é {resultado}.")
