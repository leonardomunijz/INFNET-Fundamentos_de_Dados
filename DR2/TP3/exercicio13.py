def exibir_frase_invertida_com_slicing(frase):
    """
    Inverte a frase passada como argumento utilizando o slicing
    e imprime o resultado.

    Parâmetros:
        frase (str): A frase a ser invertida.

    Retorno:
        None: Esta função apenas exibe a frase invertida no console.
    """
    frase_invertida = frase[::-1]
    print(f"Frase invertida: {frase_invertida}")

def main():
    """
    Função principal que executa o programa de inverção de frases.
    """
    frase = input("Entre com uma frase para ser invertida: ")
    exibir_frase_invertida_com_slicing(frase)

main()