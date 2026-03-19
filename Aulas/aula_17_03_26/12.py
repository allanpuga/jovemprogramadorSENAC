# Acessar elementos da tupla
#Tarefa: Leia três frutas e coloque em uma tupla. Depois leia uma fruta e diga se ela está ou não na tupla.
#Orientações: 
# usar in
# usar input()
# tipo: str, tuple
# conceito: operador de pertinência

fruta1 = input("Digite a primeira fruta: ")
fruta2 = input("Digite a segunda fruta: ")
fruta3 = input("Digite a terceira fruta: ")
tupla_frutas = (fruta1, fruta2, fruta3)
fruta_verificar = input("Digite uma fruta para verificar se está na tupla: ")
if fruta_verificar in tupla_frutas:
    print(f"A fruta '{fruta_verificar}' está na tupla.")
else:    print(f"A fruta '{fruta_verificar}' não está na tupla.")

