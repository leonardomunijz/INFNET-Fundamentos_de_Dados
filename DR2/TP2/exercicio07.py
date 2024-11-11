def exibir_lista_invertida(lista):
    """
    Exibe uma lista de forma invertida.

    Parâmetros:
        lista (list): A lista a ser exibida.

    Retorna:
        None: Esta função não retorna nenhum valor. Ela 
              apenas imprime uma mensagem no console.
    """
    print(lista[::-1], end=" ")

def main():
    """
    Função principal que gerencia o fluxo do programa.

    Exibe uma lista de forma invertida.
    """
    lista = [10, 20, 30, 40, 50, 60, 70, 80]
    exibir_lista_invertida(lista)

main()