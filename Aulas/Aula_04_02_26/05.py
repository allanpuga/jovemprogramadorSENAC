# Crie uma função que receba uma string e retorne a quantidade de caracteres que ela possui.

def contar_caracteres(string):
    return len(string)

# Exemplo de uso
texto = input("Digite uma string: ")
quantidade = contar_caracteres(texto)
print(f"A string '{texto}' possui {quantidade} caracteres.")

