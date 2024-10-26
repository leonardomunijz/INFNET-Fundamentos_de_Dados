def verificar_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(".", "")

    if texto == texto[::-1]:
        print("A palavra é um palíndromo!")
    else:
        print("A palavra não é um palíndromo!")

while True:
    texto = input("Digite uma palavra ou frase (ou 'sair' para terminar o programa): ")
    if texto.lower() == "sair":
        print("Obrigado por usar o programa! Até a próxima!")
        break

    verificar_palindromo(texto)
