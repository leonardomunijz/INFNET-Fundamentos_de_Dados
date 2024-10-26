def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    return numero1 / numero2

def dividir_inteiro(numero1, numero2):
    return numero1 // numero2

try:
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))
except ValueError:
    print("Digite apenas números inteiros!")
    exit()
else:
    print(f"A soma dos números é: {somar(numero1, numero2)}")
    print(f"A subtração dos números é: {subtrair(numero1, numero2)}")
    print(f"A multiplicação dos números é: {multiplicar(numero1, numero2)}")
    if numero2 == 0:
        print("Não é possível dividir por zero")
    else:
        print(f"A divisão dos números é: {dividir(numero1, numero2)}")
        print(f"A divisão inteira dos números é: {dividir_inteiro(numero1, numero2)}")
