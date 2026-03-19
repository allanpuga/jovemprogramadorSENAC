agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}
print("Agenda inicial:", agenda)
# Adicionar um novo contato
novo_nome = input("Digite o nome do novo contato: ")
novo_telefone = input("Digite o telefone do novo contato: ")
agenda[novo_nome] = novo_telefone
print("Agenda após adicionar novo contato:", agenda)
# Atualizar o telefone de um contato informado (se existir)
nome_atualizar = input("Digite o nome do contato para atualizar o telefone: ")
if nome_atualizar in agenda:
    novo_telefone_atualizar = input("Digite o novo telefone: ")
    agenda[nome_atualizar] = novo_telefone_atualizar
    print("Agenda após atualizar telefone:", agenda)
else:
    print("Contato não encontrado.")

# Remover um contato pelo nome (se existir)
nome_remover = input("Digite o nome do contato para remover: ")
if nome_remover in agenda:
    agenda.pop(nome_remover)
    print("Agenda após remover contato:", agenda)
else:
    print("Contato não encontrado.")

# Exibir a lista ordenada de nomes de contatos
print("Lista ordenada de nomes de contatos:", sorted(agenda.keys()))

