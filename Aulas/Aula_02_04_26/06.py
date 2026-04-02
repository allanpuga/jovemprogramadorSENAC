# Crie uma função que receba uma lista de números e retorne a média dos valores.

def media(lista):
    if not lista:  # Verifica se a lista está vazia
        return None  # Retorna None se a lista estiver vazia
    soma = sum(lista)  # Calcula a soma dos números na lista
    quantidade = len(lista)  # Obtém a quantidade de números na lista
    media = soma / quantidade  # Calcula a média
    return media
# criar lista de numeros a partir do input do usuário, se o usuário digitar "0", a lista é finalizada
numeros = []
while True:
    numero = int(input("Digite um número (ou 0 para finalizar): "))
    if numero == 0:
        break
    numeros.append(numero)

resultado = media(numeros)
print(f"A média dos números da lista é: {resultado}")

