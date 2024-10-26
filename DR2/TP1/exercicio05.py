def saudar_usuario():
    nome = input("Digite seu nome: ").strip()
    sobrenome = input("Digite seu sobrenome: ").strip()

    if not nome or not sobrenome:
        print("É necessário digitar tanto um nome quanto um sobrenome!")
        return

    mensagem = f"Olá, {nome} {sobrenome}! Seja bem-vindo(a) ao meu programa Python!"
    print(mensagem)

saudar_usuario()