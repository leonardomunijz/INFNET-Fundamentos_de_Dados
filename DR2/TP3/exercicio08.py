def contar_vogais(frase):
    """
    Conta o número de vogais em uma frase fornecida pelo usuário.

    A função conta as vogais 'a, e, i, o, u' em uma frase, incluindo
    as acentuadas 'á, é, í, ó, ú' e as com til 'ã, õ', desconsiderando
    diferenças de maiúsculas e minúsculas.

    Parâmetros:
        frase (str): A frase a qual as vogais setão contadas.

    Retorno:
        int: O número total de vogais presentes na frase.
    """
    vogais = "aeiouáéíóúãõ"
    contador_de_vogais = 0

    for letra in frase:
        if letra.lower() in vogais:
            contador_de_vogais += 1
    
    return contador_de_vogais

def main():
    """
    Função principal do programa.

    Solicita ao usuário que insira uma frase e exibe o número de vogais
    presentesna frase.
    """
    frase = input("Digite uma frase para contar o número de vogais: ")
    numero_de_vogais = contar_vogais(frase)
    print(f"A frase possui {numero_de_vogais} vogais.")

main()