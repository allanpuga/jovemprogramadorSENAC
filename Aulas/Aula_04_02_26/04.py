# Crie uma função que receba uma lista de números e retorne o maior número da lista. 

def maior_numero(lista):
    if not lista:  # Verifica se a lista está vazia
        return None  # Retorna None se a lista estiver vazia
    maior = lista[0]  # Inicializa o maior número com o primeiro elemento da lista
    for numero in lista:
        if numero > maior:
            maior = numero  # Atualiza o maior número encontrado
    return maior

# criar lista de numeros a partir do input do usuário, se o usuário digitar "0", a lista é finalizada
numeros = []
while True:
    numero = int(input("Digite um número (ou 0 para finalizar): "))
    if numero == 0:
        break
    numeros.append(numero)

resultado = maior_numero(numeros)
print(f"O maior número da lista é: {resultado}")

