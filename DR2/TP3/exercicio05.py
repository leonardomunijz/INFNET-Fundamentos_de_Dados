def verificar_ano_bissexto(ano):
    return ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0))

def validar_data(data):
    """
    Valida uma data no formato 'dd/mm/aaaa', verificando se os valores de
    dia, mês e ano são consistentes.

    A função verifica:
    - Se o formato de data está correto;
    - Se o mês está entre 1 e 12;
    - Se o dia é válido para o mês correspondente, considerando anos bissextos.

    Parâmetros:
        data (str): A data no formato 'dd/mm/aaaa' inserida pelo usuário.

    Retorno:
        bool: Retorna 'True' se a data for válida, caso contrário 'False'.
    """
    try:
        data_em_partes = data.split("/")

        if len(data_em_partes) != 3:
            print("A data deve estar no formato dd/mm/aaaa.")
        else:
            dia = int(data_em_partes[0])
            mes = int(data_em_partes[1])
            ano = int(data_em_partes[2])

            if mes < 1 or mes > 12:
                return False

            # Dicionário com o número de dias de cada mês
            dict_dias_por_mes = {
                1: 31,
                2: 28,
                3: 31,
                4: 30,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31
            }

            # Ajustes para o mês de fevereiro, em caso do ano ser bissexto
            if mes == 2 and verificar_ano_bissexto(ano):
                dict_dias_por_mes[2] = 29

            if dia < 1 or dia > dict_dias_por_mes[mes]:
                return False
            
            return True
        
    except ValueError:
        print("Erro: Você inseriu um formato de data inválido.")
        return False

def main():
    """
    Função principal do programa.

    Solicita ao usuário que insira uma data no formato 'dd/mm/aaaa',
    e utiliza a função 'validar_data()' para validar se é válida ou
    inválida.
    """
    data = input("Digite uma data no formato 'dd/mm/aaaa': ")

    if validar_data(data):
        print("Data válida!")
    else:
        print("Data inválida!")

main()