def verificar_numeros_primos(numero):
    """
    Verifica se um número é primo.

    Parâmetros:
        numero (int): O número a ser verificado.

    Retorna:
        bool: True se o número for primo, False caso contrário.
    """
    if numero < 2:
        return False
    
    rq_numero = int(numero ** 0.5)
    for i in range(2, rq_numero + 1):
        if numero % i == 0:
            return False
    
    return True

def gerar_lista_de_numeros_primos(primeiro_intervalo, ultimo_intervalo):
    """
    Gera uma lista de números primos entre dois intervalos.

    Parâmetros:
        primeiro_intervalo (int): O primeiro número do intervalo.
        ultimo_intervalo (int): O último número do intervalo.

    Retorna:
        list: Lista com os números primos entre os intervalos.
    """
    lista_numeros_primos = []

    for numero in range(primeiro_intervalo, ultimo_intervalo + 1):
        if verificar_numeros_primos(numero):
            lista_numeros_primos.append(numero)
    return lista_numeros_primos

def exibir_lista_de_numeros_primos(lista_de_numeros_primos, primeiro_intervalo, ultimo_intervalo):
    """
    Exibe os números primos encontrados entre dois intervalos.

    Parâmetros:
        lista_de_numeros_primos (list): Lista com os números primos encontrados.
        primeiro_intervalo (int): O primeiro número do intervalo.
        ultimo_intervalo (int): O último número do intervalo.

    Retorna:
        None: Esta função não retorna nenhum valor. Ela apenas imprime uma mensagem no console.
    """
    print(f"Números primos entre {primeiro_intervalo} e {ultimo_intervalo}:")
    for num in lista_de_numeros_primos:
        print(num, end=" ")
    print()
    
def exibir_quantidade_de_numeros_primos(lista_de_numeros_primos):
    """
    Exibe a quantidade de números primos encontrados.

    Parâmetros:
        lista_de_numeros_primos (list): Lista com os números primos encontrados.

    Retorna:
        None: Esta função não retorna nenhum valor. Ela apenas imprime uma mensagem no console.
    """
    print(f"Quantidade de números primos encontrada: {len(lista_de_numeros_primos)}")

def main():
    """
    Função principal que gerencia o fluxo do programa.

    Solicita dois intervalos e exibe os números primos encontrados entre eles.
    """
    while True:
        try:
            primeiro_intervalo = int(input("Digite intervalo do primeiro número: "))
            ultimo_intervalo = int(input("Digite intervalo do último número: "))

            if primeiro_intervalo > ultimo_intervalo:
                print("O primeiro intervalo deve ser menor que o último intervalo. Tente novamente.")
                continue # Volta para o início do loop se a condição for inválida

            break # Sai do loop se a entrada for válida
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros. Tente novamente.")

    lista_de_numeros_primos = gerar_lista_de_numeros_primos(primeiro_intervalo, ultimo_intervalo)
    exibir_lista_de_numeros_primos(lista_de_numeros_primos, primeiro_intervalo, ultimo_intervalo)
    exibir_quantidade_de_numeros_primos(lista_de_numeros_primos)

main()