def verificar_imc():
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))

    if peso <=0 or altura <= 0:
        print("Peso e altura devem ser positivos!")
        return

    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif imc < 25:
        print("Classificação: Peso normal")
    elif imc < 30:
        print("Classificação: Sobrepeso")
    elif imc < 35:
        print("Classificação: Obesidade grau 1")
    elif imc < 40:
        print("Classificação: Obesidade grau 2")
    else:
        print("Classificação: Obesidade grau 3")

verificar_imc()