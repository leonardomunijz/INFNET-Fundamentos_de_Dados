def calcular_soma(inicio, fim):
    """
    Calcula a soma dos números inteiros no intervalo [inicio, fim].

    Parâmetros:
        inicio (int): O primeiro número do intervalo.
        fim (int): O último número do intervalo.

    Retorna:
        int: A soma dos números inteiros no intervalo [inicio, fim].
    """
    return sum(range(inicio, (fim + 1)))

def calcular_media(inicio, fim):
    """
    Calcula a média dos números inteiros no intervalo [inicio, fim].

    Parâmetros:
        inicio (int): O primeiro número do intervalo.
        fim (int): O último número do intervalo.

    Retorna:
        float: A média dos números inteiros no intervalo [inicio, fim].
    """
    soma = calcular_soma(inicio, fim)
    quantidade = soma / ((fim - inicio) + 1)
    return soma / quantidade

def main():
    """
    Função principal que gerencia o fluxo do programa.

    Calcula e exibe a soma e a média dos números inteiros no intervalo [1, 100].
    """
    INICIO = 1
    FIM = 100

    soma = calcular_soma(INICIO, FIM)
    media = calcular_media(INICIO, FIM)

    print(f"Soma: {soma}")
    print(f"Média: {media}")

main()