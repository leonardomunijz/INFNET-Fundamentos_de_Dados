def formatar_cpf(cpf):
    """
    Formata o CPF fornecido para o formato 123.456.789-10.

    Parâmetros:
        cpf (str): o número de CPF a ser formatado.

    Retorno:
        str: O CPF no formato 123.456.789-10.
    """
    if len(cpf) == 11 and cpf.isdigit():
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    else:
        return "Erro: CPF deve ter extamente 11 digitos. Tente novamente."

def main():
    """
    Função principal do porgrama.

    Solicita ao usuário que insira um CPF e exibe o CPF formatado 
    ou uma mensagem de erro caso o CPF não tenha 11 digitos.
    """
    while True:
        cpf = input("Digite seu CPF para ser formatado: ")

        if len(cpf) == 11 and cpf.isdigit():
            cpf_formatado = formatar_cpf(cpf)
            print(f"CPF formatado: {cpf_formatado}")
            break
        else:
            print("Erro: CPF deve ter extamente 11 digitos. Tente novamente.")

main()