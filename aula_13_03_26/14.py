# Leia dias (int). Mantenha apenas os dias restantes após converter para semanas (7 dias) usando %=.

print ("Digite os dias: ")
dias = int(input())
dias %= 7
print ("O(s) dia(s) restante(s): ", dias)
