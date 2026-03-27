# Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

print("Atividade 2: Tamanho de strings")
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

print(f"Conteúdo da primeira string: {string1}")
print(f"Comprimento da primeira string: {len(string1)}")

print(f"Conteúdo da segunda string: {string2}")
print(f"Comprimento da segunda string: {len(string2)}")

if len(string1) == len(string2):
    print("As duas strings possuem o mesmo comprimento.")
else:
    print("As duas strings não possuem o mesmo comprimento.")

if string1 == string2:
    print("As duas strings são iguais no conteúdo.")
else:
    print("As duas strings são diferentes no conteúdo.")

    