import random

def lancar_dados():
    try:
        numero_de_dados = int(input("Quantos dados você quer lançar? "))

        if numero_de_dados < 1:
            print("Digite um número maior que zero!")
        else:
            for i in range(numero_de_dados):
                print(f"Dado {i + 1}: {random.randint(1, 6)}")

    except ValueError:
        print("Digite apenas números inteiros!")

while True:
    lancar_dados()
    repetir_lancamento_dados = input("Deseja lançar os dados novamente? (s/n) ").strip().lower()
    if repetir_lancamento_dados != "s":
        print("Obrigado por usar o programa! Até a próxima!")
        break