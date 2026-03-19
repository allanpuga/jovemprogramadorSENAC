# Criar e exibir dicionário de aluno. Leia nome e idade. Crie aluno = {"nome": ..., "idade": ...} e exiba o dicionário e seu tipo. Use: input(), int(), literal {}, acesso por chave dict["chave"], print(), type(). Tipos: str, int, dict. Conceitos: mapeamento chave-valor, criação e exibição.

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
aluno = {"nome": nome, "idade": idade}
print(f"Aluno: {aluno}")
print(f"Tipo do aluno: {type(aluno)}")



