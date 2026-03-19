# Leia tempo em segundos (int). Converta para minutos inteiros com //= 60 e depois use %= para obter segundos restantes.
# Solicite ao usuário que informe os tempos em segundos (int). Converta para minutos inteiros com //= e depois use %= para obter segundos restantes.  

tempo_total = int(input("Digite o tempo em segundos: "))

minutos = tempo_total
minutos //= 60

segundos = tempo_total
segundos %= 60

print("O tempo convertido é:", minutos, "minuto(s) e", segundos, "segundo(s) restante(s).")