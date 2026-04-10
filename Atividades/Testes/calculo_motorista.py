# Calcular o valor a ser pago de inss pelo motorista considerando que o valor da corrida é X, a plataforma fica com 30% o restante 25% é o valor a incidir o inss de 7.5%.
# Peça o valor da corrida e calcule o valor a ser pago de inss.
# Diga quanto fica para plataforma, quanto fica para o motorista e quanto é o valor do inss a ser pago pelo motorista.

print("Atividade 1: Cálculo do INSS para motorista")
valor_corrida = float(input("Digite o valor da corrida: R$ "))
plataforma = valor_corrida * 0.30
restante = valor_corrida - plataforma
inss = restante * 0.25 * 0.075
print("O valor a ser pago de INSS é: R$ {:.2f}".format(inss))
print("Valor para a plataforma: R$ {:.2f}".format(plataforma))
print("Valor para o motorista - INSS: R$ {:.2f}".format(restante - inss))

# Agora peça o valor de faturamento sem o valor da plataforma e calcule o valor a ser pago de inss considerando o mesmo percentual de 7.5% sobre o valor do faturamento.
# Diga quanto fica para o motorista e quanto é o valor do inss a ser pago pelo motorista.
# Diga quanto a plataforma lucrou considerando o faturamento e que ela fica com 30% do valor total.

faturamento = float(input("Digite o valor do faturamento sem o valor da plataforma: R$ "))
inss_faturamento = faturamento * 0.25 * 0.075
print("O valor a ser pago de INSS sobre o faturamento é: R$ {:.2f}".format(inss_faturamento))
print("Valor para o motorista: R$ {:.2f}".format(faturamento - inss_faturamento))
print("Lucro da plataforma: R$ {:.2f}".format((faturamento // 0.70) - faturamento))

