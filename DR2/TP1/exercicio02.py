def converter_minutos_para_horas(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    print(f"{minutos} minutos equivalem a {horas} horas e {minutos_restantes} minutos")

def converter_horas_para_minutos(horas, minutos):
    minutos_totais = horas * 60 + minutos
    print(f"{horas} horas e {minutos} minutos equivalem a {minutos_totais} minutos")

def exibir_menu():
    print("1 - Converter minutos para horas")
    print("2 - Converter horas para minutos")
    print("0 - Sair")

while True:
    exibir_menu()
    operacao = int(input("Digite a operação desejada: "))

    match (operacao):
        case 1:
            minutos = int(input("Digite a quantidade de minutos: "))
            if minutos < 0:
                print("Digite um valor positivo para os minutos")
            else:
                converter_minutos_para_horas(minutos)
        case 2:
            horas = int(input("Digite a quantidade de horas: "))
            minutos = int(input("Digite a quantidade de minutos: "))
            if horas < 0 or minutos < 0:
                print("Digite valores positivos para as horas e minutos")
            else:
                converter_horas_para_minutos(horas, minutos)
        case 0:
            print("Saindo...")
            break
        case _:
            print("Operação inválida")
