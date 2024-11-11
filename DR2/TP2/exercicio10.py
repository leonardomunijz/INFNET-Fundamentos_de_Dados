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

            if numero == 0:
                break # Sai do loop e encerra o programa ao digitar '0'
            else:
                lista_de_numeros.append(numero)
            
        except ValueError:
            print("Aceitamos apenas números inteiros.")

    return lista_de_numeros

def calcular_media(lista_de_numeros):
    """
    Calcula a média dos números inteiros fornecidos em uma lista.

    Parâmetros:
        lista_de_numeros (list): Uma lista de números inteiros.

    Retorna:
        float: A média dos números inteiros fornecidos.
    """
    if len(lista_de_numeros) == 0:
        return 0
    return sum(lista_de_numeros) / len(lista_de_numeros)

def exibir_media(media_dos_numeros):
    """
    Exibe a média dos números inteiros fornecidos.

    Parâmetros:
        media_dos_numeros (float): A média dos números inteiros fornecidos.

    Retorna:
        None: Esta função não retorna nenhum valor. Ela apenas imprime uma mensagem no console.
    """
    print(f"Média dos números: {media_dos_numeros}")

def exibir_lista_maior_ou_igual_media(lista_de_numeros):
    """
    Exibe a média dos números inteiros fornecidos e os números maiores ou iguais à média.

    Parâmetros:
        lista_de_numeros (list): Uma lista de números inteiros.
    """
    if len(lista_de_numeros) == 0:
        print("Nenhum número foi digitado.")
        return
    
    media_dos_numeros = calcular_media(lista_de_numeros)
    exibir_media(media_dos_numeros)

    print("Lista de números maiores ou iguais a média: ")
    for num in lista_de_numeros:
        if num >= media_dos_numeros:
            print(num, end=" ")

def main():
    """
    Função principal que gerencia o fluxo do programa.

    Lê números inteiros do usuário e exibe a média dos números e os números maiores ou iguais à média.
    """
    lista_de_numeros = ler_numeros()
    exibir_lista_maior_ou_igual_media(lista_de_numeros)

main()