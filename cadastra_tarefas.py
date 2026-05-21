# Cadastro de tarefas

def mostrar_tarefas():
    for indice, tarefa in enumerate(lista_tarefas):
        print(indice + 1, "-", tarefa)

lista_tarefas = []

print(f"Cadastro de Tarefas\n")

while True:
    print(f"1 - Adicionar Tarefa")
    print("2 - Ver a lista de Tarefas")
    print("3 - Remover Tarefa")
    print("4 - Sair")

    try:
        decisao = int(input("Digite o NÚMERO da operação desejada: "))
    except:
        print()
        continue

    if decisao == 1:
        while True:
            tarefa = input("Digite a tarefa ou 'sair'").strip()
            if tarefa.lower() in ["sair", "sai", "sa"]:
                break
            lista_tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso!")
            pergunta_add_tarefa = input("Deseja adicionar mais uma tarefa? ").lower()
            if pergunta_add_tarefa in ["não", "nao", "na", "nã", "n"]:
                break
            elif pergunta_add_tarefa in ["sim", "si", "s"]:
                continue

    elif decisao == 2:
        if lista_tarefas == []:
            print(f"\nA lista de tarefas está vazia...")
        else:
            print("=" * 4, "TAREFAS", "=" * 4)
            mostrar_tarefas()
            print("=" * 16)

    elif decisao == 3:
        if lista_tarefas == []:
            print(f"\nA lista de tarefas está vazia...")
        else:
            while True:
                print("=" * 4, "TAREFAS", "=" * 4)
                mostrar_tarefas()
                print("=" * 16)
                remover = input("Digite a tarefa que quer remover ou sair: ")
                if remover.lower() in ["sair", "sai", "sa"]:
                    break
                else:
                    try:
                        remover = int(remover)
                        lista_tarefas.pop(remover - 1)
                        print("Tarefa removida!")
                        pergunta_rem_tarefa = input("Deseja remover mais uma tarefa? ").lower()
                        if pergunta_rem_tarefa in ["não", "nao", "na", "nã", "n"]:
                            break
                        elif pergunta_rem_tarefa in ["sim", "si", "s"]:
                            continue
                    except:
                        print()
    elif decisao == 4:
        break
