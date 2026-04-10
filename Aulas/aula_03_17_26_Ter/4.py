# 1. Leia três notas (float) em uma lista
notas = []
for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
# 2. Calcule a média
media = sum(notas) / len(notas)
print(f"Média inicial: {media:.2f}")
# 3. Substitua a menor nota por uma nova informada
menor_nota = min(notas)
nova_nota = float(input(f"Digite a nova nota para substituir a menor ({menor_nota}): "))
notas[notas.index(menor_nota)] = nova_nota
# 4. Ordene a lista
notas.sort()
# 5. Mostre a nova média
nova_media = sum(notas) / len(notas)
print(f"Notas ordenadas: {notas}")
print(f"Nova média: {nova_media:.2f}")

