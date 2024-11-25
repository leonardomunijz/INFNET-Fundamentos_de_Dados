def verificar_palindromo(palavra):
    """
    Verifica se uma palavra é um palíndromo.

    Parâmetros:
        palavra (str): A palavra a ser verificada.

    Retorno:
        None: Esta função apenas exibe no console se a palavra é palíndromo ou não.
    """
    palavra_verificada = palavra.replace(" ", "").lower()
    
    if palavra_verificada == palavra[::-1]:
        print(f"A palavra {palavra} é um palíndromo.")
    else:
        print(f"A palavra {palavra} não é um palíndromo.")

def main():
    """
    Função principal do programa.

    Solicita ao usuário que insira uma palavra e verifica se ela é um palíndromo.
    """
    palavra = input("Digite uma palavra para verificar se é palíndromo: ")
    verificar_palindromo(palavra)

main()