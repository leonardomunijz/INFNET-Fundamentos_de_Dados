def calcular_media(numero1, numero2):
    """
    Calcula a média de dois números.

    Parâmetros:
        numero1 (float): O primeiro número.
        numero2 (float): O segundo múmero.

    Retorno:
        float: A média de dois números.
    """
    return (numero1 + numero2) / 2

def main():
    """
    Função principal que solicita dois números ao usuário, calcula a 
    média e exibe o resultado.
    """
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    media = calcular_media(numero1, numero2)

    print(f"A média dos números {numero1} e {numero2} é {media:.2f}")

main()