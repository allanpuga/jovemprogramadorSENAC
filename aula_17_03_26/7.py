# Criar e exibir dicionário de aluno. Leia nome e idade. Crie aluno = {"nome": ..., "idade": ...} e exiba o dicionário e seu tipo. Use: input(), int(), literal {}, acesso por chave dict["chave"], print(), type(). Tipos: str, int, dict. Conceitos: mapeamento chave-valor, criação e exibição.

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
aluno = {"nome": nome, "idade": idade}
print(f"Aluno: {aluno}")
print(f"Tipo do aluno: {type(aluno)}")

# Adicionar uma nova chave nota Tarefa: Partindo de um aluno com nome e idade, leia uma nota (float) e adicione a chave "nota". Exiba o dicionário.  Use: float(), input(), atribuição dict["nota"] = valor, print() Tipos: float, dict. Conceitos: atualização/adição de chave, tipos numéricos.
nota = float(input("Digite a nota do aluno: "))
aluno["nota"] = nota
print(f"Aluno atualizado: {aluno}")



