def formatar_numero_de_telefone(numero_de_telefone):
    """
    Formata o número de telefone fornecido para o formato (XX) XXXXX-XXXX.

    Parâmetros:
        numero_de_telefone (str): O número de telefone a ser formatado.

    Retorno:
        str: O número de telefone no formato (XX) XXXXX-XXXX.
    """
    if len(numero_de_telefone) == 11 and numero_de_telefone.isdigit():
        return f"({numero_de_telefone[:2]}) {numero_de_telefone[2:7]}-{numero_de_telefone[7:]}"
    else:
        return "Número inválido! Digite apenas 11 números."

def main():
    """
    Função principal do programa.

    Solicita ao usuário que insira um número de telefone e exiba o número formatado
    ou uma mensagem de erro caso o número não tenha 11 dígitos.
    """
    while True:
        numero_de_telefone = input("Digite um número de telefone (somente numeros): ")

        if len(numero_de_telefone) == 11 and numero_de_telefone.isdigit():
            numero_de_telefone_formatado = formatar_numero_de_telefone(numero_de_telefone)
            print(f"Número de telefone formatado: {numero_de_telefone_formatado}")
            break
        else:
            print("Erro: O número de telefone digitado deve contem extamente 11 dígitos. Tente novamente.")

main()