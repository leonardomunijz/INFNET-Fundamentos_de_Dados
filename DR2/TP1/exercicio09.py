def calcular_desconto(valor_compra):
    if valor_compra > 500:
        desconto = 0.25 # 25% de desconto
    elif valor_compra > 200:
        desconto = 0.15 # 15% de desconto
    elif valor_compra > 100:
        desconto = 0.1 # 10% de desconto
    else:
        desconto = 0

    valor_desconto = valor_compra * desconto
    valor_final = valor_compra - valor_desconto
    return valor_desconto, valor_final

try:
    valor_compra = float(input("Digite o valor da compra: R$"))
    if valor_compra < 0:
        print("Digite um valor positivo!")
    else:
        valor_desconto, valor_final = calcular_desconto(valor_compra)
        
        if valor_compra > 500:
            print("Parabéns! Você ganhou 25% de desconto!")
        elif valor_compra > 200:
            print("Parabéns! Você ganhou 15% de desconto!")
        elif valor_compra > 100:
            print("Parabéns! Você ganhou 10% de desconto!")
        else:
            print("Você não ganhou desconto!")

        print(f"Desconto: R${valor_desconto:.2f}")
        print(f"Valor final: R${valor_final:.2f}")

except ValueError:
    print("Digite apenas números inteiros ou decimais separados por ponto!")