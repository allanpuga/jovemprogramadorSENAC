# Crie uma função que receba uma palavra e verifique se ela é um palíndromo

def verificar_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()  # Remove espaços e converte para minúsculas
    return palavra == palavra[::-1]  # Compara a palavra com sua versão invertida
palavra = input("Digite uma palavra: ")
if verificar_palindromo(palavra):
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")

