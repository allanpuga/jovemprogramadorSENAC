def soma(a, b, c):
    soma = a + b + c
    return soma 

def media(a, b, c):
    media = (a + b + c) / 3
    return media

# Crie uma função que receba um nome como parâmetro e exiba a mensagem: 'Bem-vindo, NOME' 

def bem_vindo(nome):
    print(f'Bem-vindo, {nome}')
    nome = input("Digite seu nome: ")
    return nome

# Crie uma função que receba dois números e retorne a soma deles. 

def soma(a, b):
    soma = a + b
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: ")) 
    return soma

# Crie uma função que receba um número e informe se ele é PAR ou ÍMPAR. 

def par_ou_impar(numero):
    numero = int(input("Digite um número: "))
    resultado = par_ou_impar(numero)
    if numero % 2 == 0:
        return "PAR"
    else:
        return "ÍMPAR"
    return



