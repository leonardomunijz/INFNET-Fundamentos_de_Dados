def votar():
    votos = {"opcao1": 0, "opcao2": 0, "opcao3": 0}
    
    print("Bem-vindo ao programa de votação!")
    print("Opções disponíveis: opcao1, opcao2, opcao3")

    while True:
        voto = input("Digite a opção em que deseja votar ou 'sair' para terminar o programa: ")

        if voto in votos:
            votos[voto] += 1
            print(f"Você votou em {voto}.")
        elif voto.lower() == 'sair':
            break
        else:
            print("Opção inválida! Tente novamente.")
    
    print("\nTotal de votos:")
    for opcao, quantidade in votos.items():
        print(f"{opcao}: {quantidade} voto(s)")

votar()
