frutas = ["maçã", "banana", "laranja", "uva", "abacaxi",   "melancia", "manga", "pera", "morango", "kiwi", "abacate", "cereja", "pêssego", "ameixa", "framboesa", "mirtilo", "amora", "goiaba", "maracujá", "carambola"]
for i in range(len(frutas)):
    print(f"{i+1}: {frutas[i]}")

# Agora use while para repetir a mesma coisa
print("\nUsando while:")
i = 0
while i < len(frutas):
    print(f"{i+1}: {frutas[i]}")
    i += 1
