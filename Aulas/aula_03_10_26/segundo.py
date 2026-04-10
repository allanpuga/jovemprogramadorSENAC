# Calcular IMC e classificar de forma simples

nome = input ('Qual é o seu nome? ')
print (f'Olá, {nome}!')
peso = float(input ('Qual é o seu peso em kg? '))
altura = float(input ('Qual é a sua altura em metros? '))
imc = peso / (altura ** 2)
print (f'{nome}, seu IMC é {imc:.2f}.')

# comparação + lógicos (faixa simplificada)

baixo_peso = imc < 18.5
peso_normal = (18.5 <= imc < 25)
sobrepeso = (25 <= imc < 30)
obesidade = imc >= 30

print ('Baixo peso' , baixo_peso)
print ('Peso normal' , peso_normal)
print ('Sobrepeso' , sobrepeso)
print ('Obesidade' , obesidade)


if baixo_peso:
    print (f'{nome}, você está abaixo do peso ideal.')
elif peso_normal:
    print (f'{nome}, você está com o peso normal.')
elif sobrepeso:
    print (f'{nome}, você está com sobrepeso.')
else:    print (f'{nome}, você está com obesidade.')



