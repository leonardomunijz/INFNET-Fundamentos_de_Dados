def calcular_numeros_pares(lista_de_numeros):
    """
    Função que recebe uma lista de números e retorna uma lista com os números pares.

    Parâmetros:
        lista_de_numeros (list): lista de números inteiros.

    Retorno:
        lista_de_numeros_pares (list): lista de números inteiros pares.
    """
    lista_de_numeros_pares = []
    for item in lista_de_numeros:
        if item % 2 == 0:
            lista_de_numeros_pares.append(item)
    return lista_de_numeros_pares
    

def calcular_numeros_impares(lista_de_numeros):
    """
    Função que recebe uma lista de números e retorna uma lista com os números ímpares.

    Parâmetros:
        lista_de_numeros (list): lista de números inteiros.

    Retorno:
        lista_de_numeros_impares (list): lista de números inteiros ímpares.
    """
    lista_de_numeros_impares = []
    for item in lista_de_numeros:
        if item % 2 != 0:
            lista_de_numeros_impares.append(item)
    return lista_de_numeros_impares

def exibir_lista(lista_de_numeros):
    """
    Função que exibe os elementos de uma lista.

    Parâmetros:
        lista_de_numeros (list): lista de números inteiros.

    Retorna:
        None: Esta função não retorna nenhum valor. Ela 
              apenas imprime uma mensagem no console.
    """
    for item in lista_de_numeros:
        print(item, end=' ')

def main():
    """
    Função principal que chama as funções calcular_numeros_pares, calcular_numeros_impares e exibir_lista.

    A função calcular_numeros_pares recebe uma lista de números e retorna uma lista com os números pares.
    A função calcular_numeros_impares recebe uma lista de números e retorna uma lista com os números ímpares.
    A função exibir_lista exibe os elementos de uma lista.
    """
    lista_de_numeros = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

    listas_de_numeros_pares = calcular_numeros_pares(lista_de_numeros)
    lista_de_numeros_impares = calcular_numeros_impares(lista_de_numeros)

    print("Lista de números pares: ", end="\n")
    exibir_lista(listas_de_numeros_pares)
    print()

    print("\nLista de números ímpares: ", end="\n")
    exibir_lista(lista_de_numeros_impares)
    print()

main()