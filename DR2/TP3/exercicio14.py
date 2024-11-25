def exibir_caracteres_extraidos(frase):
    """
    Exibe os cinco primeiros e cinco últimos caracteres de uma
    frase utilizando slicing.

    Parâmetros:
        frase (str): A frase onde serão extraídos os caracteres.

    Retorno:
        None: Esta função apenas exibe os caracteres extraídos no console.
    """
    primeiros_caracteres = frase[:5]
    ultimos_caracteres = frase[-5:]

    print(f"Cinco primeiros caracteres: {primeiros_caracteres}")
    print(f"Cinco últimos caracteres: {ultimos_caracteres}")

def main():
    """
    Função principal que solicita a entrada do usuário e exibe os 
    cinco primeiros e cinco últimos caracteres da frase inserida.
    """
    frase = input("Entre com uma frase: ")
    exibir_caracteres_extraidos(frase)

main()