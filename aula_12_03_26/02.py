# Leia saldo (float) e depósito (float). Use saldo += deposito e mostre o novo saldo.
# Solicite ao usuário que informe o saldo da sua conta e o valor que será depositado; ambos os valores devem ser do tipo FLOAT. Utilize atribuição += para adicionar o deposito ao saldo da conta e exiba o novo saldo na tela.  


print ("Digite o saldo: ")
saldo = float(input())
print ("Digite o depósito: ")
deposito = float(input())
saldo += deposito
print ("O novo saldo é: ", saldo)

