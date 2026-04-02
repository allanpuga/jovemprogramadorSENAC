# Crie uma função que receba um número e informe se ele é PAR ou ÍMPAR. 

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "PAR"
    else:
        return "ÍMPAR"
numero = int(input("Digite um número: "))
resultado = par_ou_impar(numero)
print(f"O número {numero} é {resultado}.")

