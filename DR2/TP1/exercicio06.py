import random

def adivinhar_numero():
    print("Bem-vindo ao jogo de adivinhação!\nO jogo consiste em adivinhar um número entre 1 e 10.")

    while True:
        numero_secreto = random.randint(1, 10)
        tentativas = 0
        LIMITE_TENTATIVAS = 5

        while tentativas < LIMITE_TENTATIVAS:
            try:
                palpite = int(input("Digite um número entre 1 e 10: "))

                if palpite < 1 or palpite > 10:
                    print("Você deve digite um número entre 1 e 10 somente!")
                    continue

                tentativas += 1

                if palpite < numero_secreto:
                    print("O número secreto é maior!")
                elif palpite > numero_secreto:
                    print("O número secreto é menor!")
                else:
                    print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativa(s)!")
                    break
            except ValueError:
                print("Digite apenas números inteiros!")

        if tentativas == LIMITE_TENTATIVAS:
            print(f"Você esgotou suas tentativas! O número secreto era {numero_secreto}.")

        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima!")
            break

adivinhar_numero()