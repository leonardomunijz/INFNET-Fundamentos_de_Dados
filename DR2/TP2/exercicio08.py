def somar_listas(lista1, lista2):
    """
    Função que recebe duas listas de números inteiros e retorna uma nova 
    lista com a soma dos elementos das duas listas.

    Parâmetros:
        lista1 (list): A primeira lista de números inteiros.
        lista2 (list): A segunda lista de números inteiros.

    Retorna:
        list: Uma nova lista com a soma dos elementos das duas listas.
    """
    soma = []

    for i in range(len(lista1)):
        soma.append(lista1[i] + lista2[i])

    return soma

def exibir_nova_lista(nova_lista):
    """
    Função que exibe os elementos de uma lista.

    Parâmetros:
        nova_lista (list): Uma lista de números inteiros.

    Retorna:
        None: Esta função não retorna nenhum valor. Ela 
              apenas imprime uma mensagem no console.
    """
    print("Soma das 2 listas: ")
    for num in nova_lista:
        print(num, end=" ")

def main():
    """
    Função principal que gerencia o fluxo do programa.

    Cria duas listas de números inteiros e exibe uma terceira 
    lista com a soma dos elementos das duas listas.
    """
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
    lista2 = [10, 20, 30, 40, 50, 60, 70, 80]

    lista3 = somar_listas(lista1, lista2)
    exibir_nova_lista(lista3)

main()