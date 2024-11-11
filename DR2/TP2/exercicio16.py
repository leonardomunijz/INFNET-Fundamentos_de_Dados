def ler_nome():
    """
    Função que lê um nome digitado pelo usuário.

    Retorno:
        str: O nome digitado pelo usuário.
    """
    return input("Entre com o nome: ")

def ler_nota(mensagem):
    """
    Função que lê uma nota digitada pelo usuário.

    Parâmetros:
        mensagem (str): Mensagem que será exibida ao usuário.

    Retorno:
        float: A nota digitada pelo usuário.
    """
    return float(input(mensagem))

def calcular_media_do_aluno(nota1, nota2):
    """
    Função que calcula a média do aluno.

    Parâmetros:
        nota1 (float): Nota 1.
        nota2 (float): Nota 2.

    Retorno:
        float: Média do aluno.
    """
    return round(((nota1 + nota2) / 2), 1)

def verificar_e_exibir_aprovacao(media):
    """
    Função que verifica se o aluno foi aprovado ou não.

    Parâmetros:
        media (float): Média do aluno.

    Retorno:
        str: Mensagem informando se o aluno foi aprovado.
    """
    if media >= 6.0:
        print("Aluno aprovado")
    else:
        print("Aluno em prova final")

def exibir_media(media):
    """
    Função que exibe a média do aluno.

    Parâmetros:
        media (float): Média do aluno.

    Retorno:
        str: Mensagem com a média do aluno.
    """
    print(f"Média = {media}")

def calcular_media_da_turma(soma_das_medias, numero_de_alunos):
    """
    Função que calcula a média da turma.

    Parâmetros:
        soma_das_medias (float): Soma das médias dos alunos.
        numero_de_alunos (int): Número de alunos.

    Retorno:
        float: Média da turma.
    """
    if numero_de_alunos == 0:
        return 0
    return round(soma_das_medias / numero_de_alunos, 1)

def main():
    """
    Função principal que chama as funções ler_nome, ler_nota, calcular_media_do_aluno, 
    verificar_e_exibir_aprovacao, exibir_media e calcular_media_da_turma.

    A função ler_nome lê um nome digitado pelo usuário.
    A função ler_nota lê uma nota digitada pelo usuário.
    A função calcular_media_do_aluno calcula a média do aluno.
    A função verificar_e_exibir_aprovacao verifica se o aluno foi aprovado.
    A função exibir_media exibe a média do aluno.
    A função calcular_media_da_turma calcula a média da turma.
    """
    soma_das_medias = 0
    numero_de_alunos = 0

    while True:
        nome = ler_nome()

        if nome.lower() == "fim":
            break

        nota1 = ler_nota("Entre com a nota 1: ")
        nota2 = ler_nota("Entre com a nota 2: ")

        media = calcular_media_do_aluno(nota1, nota2)

        exibir_media(media)
        verificar_e_exibir_aprovacao(media)

        soma_das_medias += media
        numero_de_alunos += 1

    media_da_turma = calcular_media_da_turma(soma_das_medias, numero_de_alunos)
    print(f"Média da turma = {media_da_turma}")

main()