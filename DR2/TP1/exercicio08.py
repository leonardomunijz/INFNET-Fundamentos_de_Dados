def verificar_idade(idade):
    if idade < 18:
        print("Você é menor de idade!")
    else:
        print("Você é maior de idade!")

try:
    idade = int(input("Digite a sua idade: "))

    if idade < 0:
        print("Erro: A idade deve ser somente positiva!")
    else:
        verificar_idade(idade)

except ValueError:
    print("Por favor, você deve entrar apenas números inteiros para a idade.")
