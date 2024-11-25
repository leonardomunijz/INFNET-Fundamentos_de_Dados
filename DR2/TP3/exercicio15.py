def substituir_ponto_e_virgula_por_virgula(entrada):
    """
    Substitui todos os ';' na string por ',' e imprime o resultado.

    Parâmetros:
        entrada (str): A string de entrada contendo ';'.

    Retorno:
        None: Esta função apenas exibe a frase substituída no console.
    """
    saida = entrada.replace(";", ",")
    print(f"Saída: {saida}")

def main():
    """
    Função principal que solicita a entrada do usuário
    e realiza a substuição.
    """
    entrada = input("Entrada: ")
    substituir_ponto_e_virgula_por_virgula(entrada)

main()