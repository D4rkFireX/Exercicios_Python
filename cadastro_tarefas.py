## Cadastro simples de tarefas
# Crie um programa que mostre um menu onde o usuário
# Pode adicionar, listar, remover tarefas e sair

lista_tarefas = []

print(f"Menu de Tarefas\n")

while True:
    print(f"\n1 - Adicionar Tarefa")
    print("2 - Ver a lista de Tarefa")
    print("3 - Remover Tarefa")
    print("4 - Sair")
    decisao = int(input("Digite o número da operação que deseja: "))

    if decisao == 1:
        while True:
            tarefa = input("Adicionar Tarefa: ")
            lista_tarefas.append(tarefa)
            pergunta_add_tarefa = input("Quer adicionar mais uma tarefa? ")
            if pergunta_add_tarefa in ["não", "nao", "n"]:
                sair = True
                break
            elif pergunta_add_tarefa in ["sim", "s"]:
                sair = False
        if sair:
            continue

    elif decisao == 2:
        if lista_tarefas == []:
            print(f"\nA lista de tarefas está vazia...\n")
        else:
            for tarefa in lista_tarefas:
                print()
                print(tarefa)
                print()

    elif decisao == 4:
        break
