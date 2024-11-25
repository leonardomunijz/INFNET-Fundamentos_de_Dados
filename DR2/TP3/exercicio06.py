def exibir_data_formatada(data):
    """
    Exibe a data no formato 'dia de nome_do_mes de ano'.

    A função converte uma data no formato 'dd/mm/aaaa' para o formato
    completo com o nome do mês por extenso. O mês é convertido usando
    uma lista de neses em português.

    Parâmetros:
        data (str): A data no formato 'dd/mm/aaaa' inserida pelo usuário.

    Retorno:
        None: Esta função apenas exibe a data formatada no console.
    """
    lista_de_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    try:
        data_em_partes = data.split("/")

        if len(data_em_partes) != 3:
            print("A data deve estar no formato dd/mm/aaaa.")
        else:
            dia = int(data_em_partes[0])
            mes = int(data_em_partes[1])
            ano = int(data_em_partes[2])

            if mes < 1 or mes > 12:
                print("Mês inválid!")
            
            print(f"{dia:02d} de {lista_de_meses[mes-1]} de {ano}")
        
    except:
        print("Erro: Você inseriu uma data inválida.")

def main():
    """
    Função principal do programa.

    Solicita ao usuário que insira uma data no formato 'dd/mm/aaaa' 
    e exibe a data no formato 'dia de nome_do_mes de ano'.
    """
    data = input("Digite uma data no formato 'dd/mm/aaaa': ")
    exibir_data_formatada(data)

main()