def ler_numero():
    """
    Função que lê um número inteiro digitado pelo usuário.

    Retorno:
        numero (int): número inteiro.
    """
    while True:
        try:
            numero = int(input("Digite um número: "))
            return numero
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

def verificar_maior_ou_igual_a_zero(numero):
    """
    Função que verifica se um número é maior ou igual a zero.

    Parâmetros:
        numero (int): número inteiro.

    Retorno:
        True: se o número for maior ou igual a zero.
        False: se o número for menor que zero.
    """
    if numero >= 0:
        return True
    else:
        return False

def main():
    """
    Função principal que chama as funções ler_numero e verificar_maior_ou_igual_a_zero.

    A função ler_numero lê um número inteiro digitado pelo usuário.
    A função verificar_maior_ou_igual_a_zero verifica se o número é maior ou igual a zero.
    """
    while True:
        numero = ler_numero()

        if verificar_maior_ou_igual_a_zero(numero):
            print(f"O número {numero} é maior ou igual a zero.")
            break
        else:
            print(f"Você digitou um número negativo. Digite um número maior ou igual a zero.")

main()