def verificar_tamanho(palavra):
    if len(palavra) < 5:
        print("A palavra é curta!")
    else:
        print("A palavra é longa!")

palavra = input("Digite uma palavra: ")
verificar_tamanho(palavra)
