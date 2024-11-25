def concatenar_e_exibir_nome_completo(nome, sobrenome):
    """
    Exibe o nome completo concatenado.

    Esta função recebe dois parâmetros: 'nome' e 'sobrenome'.
    Ela concatena os dois valores com um espaço entre eles
    e imprime o resultado na tela.

    Parâmetros:
        nome (str): O primeiro nome do usuário.
        sobrenome (str): O sobrenome do usuário.

    Retorno:
        None: Esta função apenas exibe o resultado e não retorna valores.
    """
    print(f"{nome} {sobrenome}")

def main():
    """
    Função principal do programa.

    Solicita ao usuário que insira seu nome e sobrenome e, em seguida, exibe o nome completo
    concatenando ambos através da função 'concatenar_e_exibir_nome_completo()'.
    """
    nome = input("Entre com o nome: ")
    sobrenome = input("Entre com o sobrenome: ")

    concatenar_e_exibir_nome_completo(nome, sobrenome)

main()