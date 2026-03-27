# criar um teste de IMC (Índice de Massa Corporal) para calcular o IMC de uma pessoa e classificar o resultado de acordo com as categorias estabelecidas pela Organização Mundial da Saúde (OMS).
# O programa deve solicitar ao usuário que insira seu peso em kg e sua altura em metros, calcular o IMC usando a fórmula: IMC = peso / (altura * altura) e classificar o resultado de acordo com as seguintes categorias:
# - Magreza: IMC < 18.5
# - Normal: 18.5 <= IMC < 25
# - Sobrepeso: 25 <= IMC < 30
# - Obesidade: IMC >= 30

print("Atividade 3: Cálculo do IMC")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: ")) 
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

imc = calcular_imc(peso, altura)

if imc < 18.5:
    print("Seu IMC é {:.2f}, classificado como: Magreza".format(imc))
elif 18.5 <= imc < 25:
    print("Seu IMC é {:.2f}, classificado como: Normal".format(imc))
elif 25 <= imc < 30:
    print("Seu IMC é {:.2f}, classificado como: Sobrepeso".format(imc))
else:
    print("Seu IMC é {:.2f}, classificado como: Obesidade".format(imc) )

# Agora o programa calcula quantos kg precisa perder para atingir classificação "Normal" (IMC de 18.5 a 24.9) e exibe dequanto até quantos kg precisa perder.

if imc >= 25:
    peso_ideal_min = 18.5 * (altura * altura)
    peso_ideal_max = 24.9 * (altura * altura)
    kg_perder_min = peso - peso_ideal_max
    kg_perder_max = peso - peso_ideal_min
    print("Para atingir a classificação 'Normal', você precisa perder entre {:.2f} kg e {:.2f} kg.".format(kg_perder_min, kg_perder_max))
elif imc >= 18.5 and imc < 25:
    print("Você já está na classificação 'Normal'.")
else:
    peso_ideal_min = 18.5 * (altura * altura)
    peso_ideal_max = 24.9 * (altura * altura)
    kg_ganhar_min = peso_ideal_min - peso
    kg_ganhar_max = peso_ideal_max - peso
    print("Para atingir a classificação 'Normal', você precisa ganhar entre {:.2f} kg e {:.2f} kg.".format(kg_ganhar_min, kg_ganhar_max))

