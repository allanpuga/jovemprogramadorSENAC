def meu_max(*args, key=None):
    """
    Implementação simplificada da função max() do Python.
    Aceita múltiplos argumentos ou um único iterável.
    """
    # Se apenas um argumento for passado, ele deve ser um iterável
    if len(args) == 1:
        try:
            iterator = iter(args[0])
        except TypeError:
            raise TypeError("O argumento deve ser iterável")
    else:
        iterator = iter(args)

    try:
        maior = next(iterator)  # Primeiro elemento
    except StopIteration:
        raise ValueError("max() recebeu um iterável vazio")

    # Função de chave (key) para comparação
    if key is None:
        for elemento in iterator:
            if elemento > maior:
                maior = elemento
    else:
        maior_chave = key(maior)
        for elemento in iterator:
            valor_chave = key(elemento)
            if valor_chave > maior_chave:
                maior = elemento
                maior_chave = valor_chave

    return maior

# Insira numeros e digite 0 para finalizar
numeros = []
while True:
    num = int(input("Digite um número (0 para finalizar): "))
    if num == 0:
        break
    numeros.append(num)
if numeros:
    print("O maior número digitado é:", meu_max(numeros))

# Digite palavras e digite "fim" para finalizar
palavras = []
while True:
    palavra = input("Digite uma palavra (fim para finalizar): ")
    if palavra.lower() == "fim":
        break
    palavras.append(palavra)
if palavras:
    print("A maior palavra digitada é:", meu_max(palavras))




# Exemplos de uso
print(meu_max(3, 7, 2))  # 7
print(meu_max([1, 5, 3]))  # 5
print(meu_max(["banana", "maçã", "uva"], key=len))  # "banana"
