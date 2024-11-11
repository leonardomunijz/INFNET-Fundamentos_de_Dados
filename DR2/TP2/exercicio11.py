def buscar_elemento(lista_de_numeros, numero):
    """
    Busca um número em uma lista de números inteiros e retorna
    o índice da primeira ocorrência do número na lista.

    Parâmetros:
        lista_de_numeros (list): Uma lista de números inteiros.
        numero (int): O número inteiro a ser buscado na lista.

    Retorna:
        int: O índice da primeira ocorrência do número na lista,
             ou -1 se o número não for encontrado.
    """
    if numero in lista_de_numeros:
        return lista_de_numeros.index(numero)
    else:
        return -1

def main():
    """
    Função principal que gerencia o fluxo do programa.

    Busca um número em uma lista de números inteiros e exibe a posição
    em que o número foi encontrado na lista.
    O programa continua solicitando números até que o usuário insira 
    um número que esteja na lista, momento em que o programa termina.

    """
    lista_de_numeros = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100]

    while True:
        try:
            numero = int(input("Digite um número para buscar na lista: "))
        
            resultado_e_indice = buscar_elemento(lista_de_numeros, numero)
            if resultado_e_indice != -1:
                print(f"O número {numero} foi encontrado na posição {resultado_e_indice}.")
                break # Sai do loop e encerra o programa ao encontrar o número da lista
            else:
                print(f"O número {numero} não foi encontrado na lista.")

        except ValueError:
            print("Digite apenas números inteiros.")

main()
