def verificar_vogais(caractere):
    """
    Verifica se um caractere é uma vogal.

    Parâmetros:
        caractere (str): O caractere a ser verificado.

    Retorna:
        bool: True se o caractere for uma vogal, False caso contrário.
    """
    return caractere.lower() in "aeiou"

def contar_numero_de_vogais():
    """
    Conta o número de vogais inseridas pelo usuário.

    Retorna:
        int: O número de vogais inseridas pelo usuário.
    
    Encerra o programa ao digitar '.'.
    """
    contador_de_vogais = 0

    while True:
        caractere = input("Entre com um caractere: ")

        if caractere == ".":
            break # Sai do loop e encerra o programa ao digitar '.'

        if verificar_vogais(caractere):
            contador_de_vogais += 1

    return contador_de_vogais

def main():
    """
    Função principal que gerencia o fluxo do programa.

    Chama a função contar_numero_de_vogais e exibe o resultado.
    """
    numero_de_vogais = contar_numero_de_vogais()
    print(f"Número de vogais: {numero_de_vogais}")

main()