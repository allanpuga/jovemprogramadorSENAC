
numeros = []
for i in range(10):
    num = int(input(f"Informe o {i+1}° numero inteiro: "))
    numeros.append(num)


print("\nClassificação dos números:")
for num in numeros:
    if num > 10:
        print(f"\033[92m O numero {num:.0f} é maior que 10\033[0m")  # Verde
    elif num == 10:
        print(f"\033[93m O numero {num:.0f} é igual a 10\033[0m")  # Amarelo
    else:
        print(f"\033[94m O numero {num:.0f} é menor que 10\033[0m")  # Azul

