def converter_dia_da_semana(numero_digitado):
    """
    Recebe um número entre 1 e 7, e retorna o dia da semana correspondente.

    Parâmetros:
        numero_digitado (int): O número representando o dia da semana ( 1 -> Domingo, 7 -> Sábado).

    Retorno:
        str: O nome do dia da semana correspondente ao número fornecido.
    """
    # Dicionário com os dias da semana.
    dict_dias_da_semana = {
        1: "Domingo",
        2: "Segunda-feira",
        3: "Terça-feira",
        4: "Quarta-feira",
        5: "Quinta-feira",
        6: "Sexta-feira",
        7: "Sábado"
    }

    if numero_digitado in dict_dias_da_semana:
        return dict_dias_da_semana[numero_digitado]
    else:
        return "Erro: número inválido."

def main():
    """
    Função principal do programa.

    Solicita ao usuário que insira um número entre 1 e 7 e exibe
    o dia da semana correspondente. Caso o número seja inválido,
    exibe uma mensagem de erro.
    """
    try:
        numero_digitado = int(input("Entre com um número: "))
        resultado = converter_dia_da_semana(numero_digitado)
        print(resultado)
    except ValueError:
        print("Erro: número inválido.")

main()