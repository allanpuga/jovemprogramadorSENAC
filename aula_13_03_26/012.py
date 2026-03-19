# Leia metros (int). Converta para km inteiros com //= 1000 e guarde metros restantes com %= (em outra variável).
# Solicite ao usuário uma distância em metros e depois converta para km inteiros com //= 1000, guarde os metros restantes utilizando %= (utilize outra variável).  

print ("Digite a distância em metros: ")
metros = int(input())
km = metros
km //= 1000
metros_restantes = metros
metros_restantes %= 1000
print ("A distância é: ", km, "km e", metros_restantes, "metros restantes.")

