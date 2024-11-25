def exibir_nome_formatado(nome_completo):
    """
    Formata o nome completo para o formato 'SOBRENOME, Nome'.

    A entrada deve ter pelo menos duas palavras: 'nome' e 'sobrenome'.
    A função divide o nome completo utilizando o método 'split()' e
    exibe o sobrenome em letras maiúsculas e o nome com a primeira
    letra maiúscula.

    Parâmetros:
        nome_completo (str): O nome completo inserido pelo usuário.

    Retorno:
        None: Esta função apenas exibe o nome formatado no console.
    """
    nome_separado = nome_completo.split()
    nome = nome_separado[0].capitalize()
    sobrenome = nome_separado[1].upper()
    print(f"{sobrenome}, {nome}")

def main():
    """
    Função principal do programa.

    Solicita ao usuário que insira um nome completo e exibe o nome formatado
    'SOBRENOME, Nome' utlizando a função 'exibir_nome_formatado()'. 
    """
    nome_completo = input("Digite seu nome completo (nome e sobrenome): ")
    exibir_nome_formatado(nome_completo)

main()