def validar_nome_completo(nome_completo):
    """
    Valida se o nome completo tem um nome e sobrenome com pelo menos 2 carcateres cada.

    Parâmetros:
        nome_completo (str): A string contendo o nome completo inserido pelo usuário.

    Retorno:
        bool: Retorna 'True' se a entrada for válida, caso contrário 'False'.
    """
    dividir_nome = nome_completo.split()

    # Verifica se há pelo menos 2 partes: nome e sobrenome
    if len(dividir_nome) < 2:
        return False
    
    nome, sobrenome = dividir_nome[0], dividir_nome[1]
    return len(nome) >= 2 and len(sobrenome) >= 2

def  main():
    """
    Função principal do programa.

    Solicita ao usuário que insira um nome completo (nome e sobrenome em uma linha),
    valida a entrada através da função 'validar_nome_completo()', e exibe uma mensagem
    indicando se a mesma é válida ou inválida.
    """
    nome_completo = input("Entre com o nome e sobrenome: ")

    if validar_nome_completo(nome_completo):
        print("Entrada válida!")
    else:
        print("Entrada invállida!")

main()