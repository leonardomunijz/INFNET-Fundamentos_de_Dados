def exibir_frase_invertida(frase):
    """
    Inverte a frase passada como argumento e imprime o resultado.

    Parâmetros:
        frase (str): A frase a ser invertida.

    Retorno:
        None: Esta função apenas exibe a frase invertida no console.
    """
    frase_invertida = ""

    for i in range(len(frase) - 1, -1, -1):
        frase_invertida += frase[i]

    print(f"Frase invertida: {frase_invertida}")

def main():
    """
    Função principal que executa o programa de inversão de frases.
    """
    frase = input("Entre com uma frase para ser invertida: ")
    exibir_frase_invertida(frase)

main()