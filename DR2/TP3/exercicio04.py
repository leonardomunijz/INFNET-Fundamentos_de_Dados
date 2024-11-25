def extrair_data(data):
    """
    Extrai e exibe o dia, mês e ano de uma data no formato 'dd/mm/aaaa'.

    A entrada deve ser uma string no formato 'dd/mm/aaaa'. A função divide
    a data usando o separador '/', convertendo cada parte em inteiros e 
    exibe os valores como dia, mês e ano.

    Parâmetros:
        data (str): A data no formato 'dd/mm/aaaa' inserida pelo usuário.

    Retorno:
        None: Apenas exibe os valores no console: dia, mês e ano.
    """
    try:
        data_em_partes = data.split("/")

        if len(data_em_partes) != 3:
            print("A data deve estar no formato dd/mm/aaaa.")
        else:
            dia = int(data_em_partes[0])
            mes = int(data_em_partes[1])
            ano = int(data_em_partes[2])

            print(f"Dia: {dia}")
            print(f"Mês: {mes}")
            print(f"Ano: {ano}")
        
    except ValueError:
        print("Erro: Você inseriu uma data inválida.")

def main():
    """
    Função principal do programa.

    Solicita ao usuário que insira uma data no formato 'dd/mm/aaaa',
    e utiliza a função 'extrair_data()' para exibir o dia, mês e ano
    como inteiros.
    """
    data = input("Digite uma data no formato 'dd/mm/aaaa': ")
    extrair_data(data)

main()