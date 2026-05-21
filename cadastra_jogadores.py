## Cadastro de jogadores usando while, array, append, objeto e for

lista_jogadores = [] # Array com a lista de jogadores

while True:
    while True:
        pergunta = input("Deseja cadastrar? ").lower()
        if pergunta in ["não", "nao", "n"]:
            sair = True
            break
        elif pergunta in ["sim", "s"]:
            sair = False
            break
    if sair:
        break

    jogador = {
        "nome": "",
        "idade": "",
        "nickname": ""
    }

    jogador["nome"] = input("Qual o nome? ")
    jogador["idade"] = int(input("Qual a idade? "))
    jogador["nickname"] = input("Qual o nickname? ")

    lista_jogadores.append(jogador)

    while True:
        pergunta_lista = input("Deseja ver a lista de jogadores? ").lower()
        if pergunta_lista in ["não", "nao", "n"]:
            sair = True
            break
        elif pergunta_lista in ["sim", "s"]:
            for jogador in lista_jogadores:
                print(f"-" * 20)
                print(f"Nome: ", jogador["nome"])
                print(f"Idade: ", jogador["idade"])
                print(f"Nickname", jogador["nickname"])
        if sair:
            break