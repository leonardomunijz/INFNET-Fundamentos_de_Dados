def iniciar_historia():
    print("Você está em uma floresta mágica. O sol está se pondo e você vê dois caminhos à sua frente.")
    print("1. Seguir pelo caminho da esquerda.")
    print("2. Seguir pelo caminho da direita.")

    escolha1 = int(input("Qual caminho você escolhe? (1 ou 2): "))

    match escolha1:
        case 1:
            print("Você segue pelo caminho da esquerda e encontra uma linda lagoa.")
            print("1. Nadar na lagoa.")
            print("2. Sentar e descansar.")

            escolha2 = int(input("O que você escolhe fazer? (1 ou 2): "))
            
            match escolha2:
                case 1:
                    print("Você nada na lagoa e encontra um tesouro submerso! Parabéns!")
                case 2:
                    print("Enquanto você descansa, um espírito da floresta aparece e te oferece um desejo!")
                case _:
                    print("Escolha inválida. A aventura termina aqui.")

        case 2:
            print("Você segue pelo caminho da direita e chega a uma caverna escura.")
            print("1. Entrar na caverna.")
            print("2. Voltar para a floresta.")

            escolha2 = input("O que você faz? (1 ou 2): ")

            match escolha2:
                case "1":
                    print("Dentro da caverna, você encontra criaturas mágicas que precisam de sua ajuda!")
                case "2":
                    print("Você volta para a floresta e encontra uma festa de criaturas mágicas!")
                case _:
                    print("Escolha inválida. A aventura termina aqui.")

        case _:
            print("Opção inválida! Tente novamente.")
            iniciar_historia()

iniciar_historia()