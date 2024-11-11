def achar_menor_numero(lista_de_numeros):
    """
    Encontra o menor número em uma lista de números inteiros.

    Parâmetros:
        lista_de_numeros (list): Uma lista de números inteiros.

    Retorna:
        int: O menor número encontrado na lista.
    """
    menor_numero_econtrado = lista_de_numeros[0]
    for numero in lista_de_numeros:
        if numero < menor_numero_econtrado:
            menor_numero_econtrado = numero
    return menor_numero_econtrado

def achar_maior_numero(lista_de_numeros):
    """
    Encontra o maior número em uma lista de números inteiros.

    Parâmetros:
        lista_de_numeros (list): Uma lista de números inteiros.

    Retorna:
        int: O maior número encontrado na lista.
    """
    maior_numero_encontrado = lista_de_numeros[0]
    for numero in lista_de_numeros:
        if numero > maior_numero_encontrado:
            maior_numero_encontrado = numero
    return maior_numero_encontrado

def calcular_soma_dos_numeros(lista_de_numeros):
    """
    Calcula a soma dos números inteiros fornecidos em uma lista.

    Parâmetros:
        lista_de_numeros (list): Uma lista de números inteiros.

    Retorna:
        int: A soma dos números inteiros fornecidos.
    """
    soma_dos_numeros = 0
    for numero in lista_de_numeros:
        soma_dos_numeros += numero
    return soma_dos_numeros

def calcular_media_dos_numeros(lista_de_numeros):
    """
    Calcula a média dos números inteiros fornecidos em uma lista.

    Parâmetros:
        lista_de_numeros (list): Uma lista de números inteiros.

    Retorna:
        float: A média dos números inteiros fornecidos.
    """
    media_dos_numeros = calcular_soma_dos_numeros(lista_de_numeros) / len(lista_de_numeros)
    return media_dos_numeros

def main():
    """
    Função principal que gerencia o fluxo do programa.

    Encontra o menor e o maior número em uma lista de números inteiros,
    calcula a soma dos números e a média dos números.
    """
    lista_de_numeros = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]

    menor_numero = achar_menor_numero(lista_de_numeros)
    maior_numero = achar_maior_numero(lista_de_numeros)
    soma_dos_numeros = calcular_soma_dos_numeros(lista_de_numeros)
    media_dos_numeros = calcular_media_dos_numeros(lista_de_numeros)

    print(f"Menor número da lista: {menor_numero}")
    print(f"Maior número da lista: {maior_numero}")
    print(f"Soma dos números da lista: {soma_dos_numeros}")
    print(f"Média dos números da lista: {media_dos_numeros}")

main()