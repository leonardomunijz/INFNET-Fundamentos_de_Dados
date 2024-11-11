def calcular_pa(primeiro_termo, segundo_termo, quantidade_de_termos):
    """
    Calcula os termos de uma progressão aritmética (P.A.).

    Parâmetros:
        primeiro_termo (int): O primeiro termo da P.A.
        segundo_termo (int): O segundo termo da P.A.
        quantidade_de_termos (int): A quantidade de termos da P.A.

    Retorna:
        list: Uma lista com os termos da P.A.
    """
    razao = segundo_termo - primeiro_termo
    lista_pa = [primeiro_termo + i * razao for i in range(quantidade_de_termos)]
    return lista_pa

def exibir_lista_pa(lista_pa):
    """
    Exibe os termos de uma progressão aritmética (P.A.).

    Parâmetros:
        lista_pa (list): Uma lista com os termos da P.A.

    Retorna:
        None: Esta função não retorna nenhum valor. Ela 
              apenas imprime uma mensagem no console.
    """
    print("Sequência da P.A.: ")
    for termo in lista_pa:
        print(termo, end=" ")
    print()

def main():
    """
    Função principal que gerencia o fluxo do programa.

    Solicita o primeiro termo, o segundo termo e a quantidade de termos de uma P.A.
    Exibe os termos da P.A. com base nas entradas do usuário.
    """
    while True:
        try:
            primeiro_termo = int(input("Digite o primeiro termo: "))
            segundo_termo = int(input("Digite o segundo termo: "))
            quantidade_de_termos = int(input("Digite a quantidade de termos: "))

            if quantidade_de_termos < 1:
                print("A quantidade de termos deve ser maior que zero. Tente novamente.")
                continue  # Volta para o início do loop se a quantidade for inválida

            break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros. Tente novamente.")
    
    lista_pa = calcular_pa(primeiro_termo, segundo_termo, quantidade_de_termos)
    exibir_lista_pa(lista_pa)

main()