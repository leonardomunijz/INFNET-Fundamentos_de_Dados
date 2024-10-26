def exibir_menu():
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

def escolher_operacao():
    return int(input("Digite a operação desejada: "))

def entrar_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite apenas números")

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"A soma dos números é: {resultado}")

def subtrair(numero1, numero2):
    resultado = numero1 - numero2
    print(f"A subtração dos números é: {resultado}")

def multiplicar(numero1, numero2):
    resultado = numero1 * numero2
    print(f"A multiplicação dos números é: {resultado}")

def dividir(numero1, numero2):
    if numero2 == 0:
        print("Não é possível dividir por zero")
    else:
        resultado = numero1 / numero2
        print(f"A divisão dos números é: {resultado}")

while True:
    exibir_menu()
    operacao = escolher_operacao()

    if operacao == 0:
        print("Saindo...")
        break
    elif operacao < 1 or operacao > 4:
        print("Operação inválida. Tente novamente.")
    else:
        numero1 = entrar_numero("Digite um nímero: ")
        numero2 = entrar_numero("Digite outro nímero: ")

        match (operacao):
            case 1:
                somar(numero1, numero2)
            case 2:
                subtrair(numero1, numero2)
            case 3:
                multiplicar(numero1, numero2)
            case 4:
                dividir(numero1, numero2)

