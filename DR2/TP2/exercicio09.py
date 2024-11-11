def ler_numeros():
    """
    Lê uma sequência de números inteiros fornecidos pelo usuário e os armazena em uma lista.
    O programa continua solicitando números até que o usuário insira o número '0', 
    momento em que o programa termina e retorna a lista de números.

    Durante a entrada, o programa valida se os valores inseridos são inteiros e exibe
    uma mensagem de erro se o usuário inserir um valor não inteiro.

    Retorna:
        list: Uma lista contendo os números inteiros fornecidos pelo usuário, 
              excluindo o '0' que é utilizado para terminar a entrada.
    
    Exceções:
        ValueError: Se o usuário inserir um valor que não pode ser convertido para um inteiro,
                    o programa exibe uma mensagem de erro e solicita nova entrada.
    """
    lista_de_numeros = []

    while True:
        try:
            numero = int(input("Digite um número (ou '0' para terminar o programa): "))
        except ValueError:
            print("Digite apenas números inteiros.")
        else:
            if numero == 0:
                break # Sai do loop e encerra o programa ao digitar '0'
            else:
                lista_de_numeros.append(numero)

    return lista_de_numeros

def exibir_lista_invertida(lista_de_numeros):
    """
    Exibe uma lista de números em ordem invertida.

    Parâmetros:
        lista_de_numeros (list): Uma lista de números inteiros.

    Retorna:
        None: Esta função não retorna nenhum valor. Ela apenas 
              imprime uma mensagem no console.
    """
    print("Lista em ordem invertida: ")
    for num in reversed(lista_de_numeros):
        print(num, end=" ")

def main():
    """
    Função principal que gerencia o fluxo do programa.

    Lê números inteiros do usuário e exibe a lista em ordem invertida.
    """
    lista_de_numeros = ler_numeros()
    exibir_lista_invertida(lista_de_numeros)

main()