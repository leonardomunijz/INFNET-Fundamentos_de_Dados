def verificar_par_impar(numero):
    if numero % 2 == 0:
        print("O número é par!")
    else:
        print("O número é ímpar!")

while True:
    numero = input("Digite um número ou 'sair' para terminar o programa: ")
        
    if numero == "sair":
        print("Obrigado por usar o programa! Até a próxima!")
        break
        
    verificar_par_impar(int(numero))
