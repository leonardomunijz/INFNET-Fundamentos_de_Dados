def calcular_tabuada(numero, inicio, fim):
    """
    Função que calcula a tabuada de um número.

    Parâmetros:
        numero (int): número para o qual a tabuada será calculada
        inicio (int): início da tabuada
        fim (int): fim da tabuada

    Retorno:
        list: lista com os resultados da tabuada
    """
    return [numero * i for i in range(inicio, (fim + 1))]

def exibir_tabuada(numero, lista_resultados, inicio, fim):
    """
    Função que exibe a tabuada de um número.

    Parâmetros:
        numero (int): número para o qual a tabuada será exibida
        lista_resultados (list): lista com os resultados da tabuada
        inicio (int): início da tabuada
        fim (int): fim da tabuada

    Retorna:
        None: Esta função não retorna nenhum valor. Ela
              apenas imprime uma mensagem no console.
    """
    print(f"--- Tabuada do {numero} ---")
    for i in range(inicio, (fim + 1)):
        print(f"    {numero} x {i} = {lista_resultados[i - 1]}")
    print()

def main():
    """
    Função principal do programa.

    Exibe a tabuada dos números de 1 a 10.
    """
    INICIO = 1
    FIM = 10

    for numero in range(INICIO, (FIM + 1)):
        lista_resultados = calcular_tabuada(numero, INICIO, FIM)
        exibir_tabuada(numero, lista_resultados, INICIO, FIM)

main()