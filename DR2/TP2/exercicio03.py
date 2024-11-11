def calcular_fatorial(n):
    """
    Calcula o fatorial de um número inteiro positivo.

    Parâmetros:
        n (int): O número inteiro positivo.

    Retorna:
        int: O fatorial do número inteiro positivo.
    """
    if n == 0 or n == 1:
        return 1
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial

def main():
    """
    Função principal que gerencia o fluxo do programa.

    Solicita um número inteiro positivo ao usuário e exibe o fatorial do número.
    O programa continua até que o usuário insira '0'.
    """
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo (ou '0' para terminar o programa): "))
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
            continue # Continua o loop para tentar novamente

        if numero == 0:
            print("Obrigado por usar o programa! Até a próxima!")
            break # Sai do loop e encerra o programa ao digitar '0'
        elif numero < 0:
            print("Por favor, ensira somente números positivos.")
        else:
            fatorial = calcular_fatorial(numero)
            print(f"O fatorial do número {numero} é {fatorial}")

main()