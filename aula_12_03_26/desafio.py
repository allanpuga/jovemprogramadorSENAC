print("Bem-vindo ao Sistema de Recomendação de Cursos!")
print("-" * 50)

# 1. Pergunte algumas informações do usuário
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

# Usamos .strip().lower() para remover espaços extras e garantir que a resposta fique em minúsculo
ja_programou = input("Você já programou antes? (sim/nao): ").strip().lower()
preferencia = input("Você gosta mais de lógica ou design? (logica/design): ").strip().lower()
tem_computador = input("Você tem computador em casa? (sim/nao): ").strip().lower()
interesse_design = input("Você tem interesse em design? (sim/nao): ").strip().lower()

print("-" * 50)
print(f"Analisando o perfil de {nome}...\n")

# 2. Analise as respostas usando operadores lógicos e 3. Recomende um curso
if tem_computador == "nao":
    print("Recomendação: Curso de Introdução à Informática.")
    print("Motivo: Ideal para se familiarizar com computadores antes de começar a programar ou desenhar telas.")

elif preferencia == "logica" and ja_programou == "nao":
    print("Recomendação: Curso de Lógica de Programação.")
    print("Motivo: Perfeito para quem tem perfil analítico e está dando os primeiros passos na área.")

elif preferencia == "logica" and ja_programou == "sim":
    print("Recomendação: Curso de Desenvolvimento Back-End com Python.")
    print("Motivo: Como você já sabe o básico e gosta de lógica, está pronto para criar sistemas reais!")

elif (preferencia == "design" or interesse_design == "sim") and ja_programou == "nao":
    print("Recomendação: Curso de UX/UI Design.")
    print("Motivo: Focado puramente na parte visual e na experiência do usuário, sem necessidade de código inicial.")

elif (preferencia == "design" or interesse_design == "sim") and ja_programou == "sim":
    print("Recomendação: Curso de Desenvolvimento Front-End (HTML/CSS/JS).")
    print("Motivo: Une o seu interesse visual com a sua experiência prévia em programação.")

else:
    print("Recomendação: Curso de Descoberta Tecnológica.")
    print("Motivo: Um curso geral para ajudar a explorar as diferentes áreas da tecnologia.")

print("\nObrigado por usar o Sistema de Recomendação de Cursos, " + nome + "!")

