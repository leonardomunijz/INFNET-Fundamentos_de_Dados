def exibir_menu():
    """
    Exibe o menu de opções disponíveis para o usuário.

    Esta função imprime as opções disponíveis para o usuário interagir com o programa.
    O menu inclui a possibilidade de adicionar uma nova tarefa, listar as tarefas existentes,
    marcar uma tarefa como concluída, remover uma tarefa específica ou sair do programa.
    """
    print("\nMenu de Opções: ")
    print("[1] - Adicionar Tarefa")
    print("[2] - Listar Tarefas")
    print("[3] - Marcar Tarefa como Concluída")
    print("[4] - Remover Tarefa")
    print("[0] - Sair")

def obter_escolha():
    """
    Obtém a escolha do usuário a partir do menu de opções.

    Esta função exibe uma solicitação para o usuário escolher uma opção do menu. 
    Se a entrada for válida (um número inteiro), a função retorna a opção escolhida.
    Caso a entrada seja inválida (não um número inteiro), a função imprime uma mensagem de erro 
    e retorna `None`.

    Retorna:
        int: A opção escolhida pelo usuário. 
        Caso a entrada seja inválida, retorna `None`.
    """
    try:
        return int(input("Escolha uma opção: "))
    except ValueError:
        print("Entrada inválida! Digite um número válido.")
        return None
    
def obter_id(mensagem):
    """
    Solicita ao usuário uma entrada numérica a partir de uma mensagem.

    Esta função exibe uma mensagem solicitando ao usuário que insira um número inteiro.
    Se a entrada for válida, a função retorna o valor como um número inteiro.
    Caso contrário, exibe uma mensagem de erro informando que a entrada é inválida e retorna `None`.

    Parâmetros:
        mensagem (str): A mensagem a ser exibida ao usuário.

    Retorna:
        int: O número inteiro inserido pelo usuário, caso a entrada seja válida.
        None: Se a entrada for inválida (não numérica).
    """
    try:
        return int(input(mensagem))
    except ValueError:
        print("Entrada inválida! Digite um número válido.")
        return None

def adicionar_tarefa(lista_de_tarefas):
    """
    Adiciona uma nova tarefa à lista de tarefas.

    Parâmetros:
        lista_de_tarefas (list): Lista contendo dicionários de tarefas
                                  com informações como ID, descrição e status.

    O ID da tarefa é gerado automaticamente com base no maior ID da lista,
    ou iniciado como 1 se a lista estiver vazia.
    """
    descricao_da_nova_tarefa = input("Digite a descrição da nova tarefa: ")

    if lista_de_tarefas:
        id_tarefa = (max(tarefa['id'] for tarefa in lista_de_tarefas) + 1)
    else:
        id_tarefa = 1

    lista_de_tarefas.append({'id': id_tarefa, 'descricao': descricao_da_nova_tarefa, 'status': 'Pendente'})
    print(f"Tarefa '{descricao_da_nova_tarefa}' com o ID {id_tarefa} foi adicionada com sucesso!")

def listar_tarefas(lista_de_tarefas):
    """
    Exibe a lista de tarefas pendentes.

    Esta função percorre a lista de tarefas e imprime a descrição de cada uma, 
    juntamente com seu status atual. Se a lista estiver vazia, uma mensagem 
    informando que não há tarefas será exibida.

    Parâmetros:
        lista_de_tarefas (list): Lista de dicionários, onde cada dicionário 
                                  representa uma tarefa com as chaves 'id', 
                                  'descricao' e 'status'.

    Comportamento:
        - Se a lista de tarefas estiver vazia, imprime "Nenhuma tarefa adicionada ainda."
        - Caso contrário, imprime a lista de tarefas, exibindo o ID, descrição 
          e o status de cada tarefa.
    """
    if not lista_de_tarefas:
        print("Nenhuma tarefa adicionada ainda.")
    else:
        print("Lista de tarefas pendentes: ")
        for tarefa in lista_de_tarefas:
            print(f"{tarefa['id']}. {tarefa['descricao']} - Status: {tarefa['status']}")

def marcar_como_concluida(lista_de_tarefas):
    """
    Marca uma tarefa específica como concluída.

    Esta função solicita ao usuário um ID de tarefa por meio da função `obter_id()`
    para marcar a tarefa correspondente como concluída. Se a tarefa já estiver
    concluída ou se o ID fornecido não for encontrado, uma mensagem de erro será
    exibida. Caso contrário, a tarefa terá seu status alterado para "Concluída".

    Parâmetros:
        lista_de_tarefas (list): Lista de dicionários, onde cada dicionário 
                                  representa uma tarefa com as chaves 'id', 
                                  'descricao' e 'status'.

    Comportamento:
        - Se a lista de tarefas estiver vazia, exibe "Nenhuma tarefa para marcar como concluída."
        - Solicita o ID da tarefa usando a função `obter_id()`.
        - Se o ID informado não corresponder a nenhuma tarefa, exibe "ID da tarefa não encontrado!"
        - Se a tarefa já estiver concluída, exibe "Essa tarefa já está concluída."
        - Caso contrário, altera o status da tarefa para "Concluída" e exibe a confirmação.
    """
    if not lista_de_tarefas:
        print("Nenhuma tarefa para marcar como concluída.")
        return
    
    try:
        id_tarefa = obter_id("Digite o ID da tarefa para marcar como concluída: ")

        tarefa_encontrada = next((tarefa for tarefa in lista_de_tarefas if tarefa['id'] == id_tarefa), None)

        if tarefa_encontrada:
            if tarefa_encontrada['status'] == "Pendente":
                tarefa_encontrada['status'] = "Concluída"
                print(f"Tarefa com ID {id_tarefa} foi marcada como concluída!")
            else:
                print("Essa tarefa já está concluída.")
        else:
            print("ID da tarefa não encontrado!")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

def remover_tarefa(lista_de_tarefas):
    """
    Remove uma tarefa da lista com base no ID fornecido.

    Esta função solicita ao usuário um ID de tarefa por meio da função `obter_id()`
    para remover a tarefa correspondente. Se o ID fornecido não for encontrado
    ou se for inválido, uma mensagem de erro será exibida. Caso contrário, a
    tarefa será removida da lista.

    Parâmetros:
        lista_de_tarefas (list): Lista de dicionários, onde cada dicionário 
                                  representa uma tarefa com as chaves 'id', 
                                  'descricao' e 'status'.

    Comportamento:
        - Se a lista de tarefas estiver vazia, exibe "Não há tarefas para remover."
        - Solicita o ID da tarefa usando a função `obter_id()`.
        - Se o ID fornecido não corresponder a nenhuma tarefa, exibe "ID da tarefa inválido!"
        - Caso contrário, remove a tarefa da lista e exibe uma mensagem de sucesso.
    """
    if not lista_de_tarefas:
        print("Não há tarefas para remover.")
        return

    try:
        id_tarefa = obter_id("Digite o número do ID da tarefa para removê-la: ")

        tarefa_a_remover = None

        for tarefa in lista_de_tarefas:
            if tarefa['id'] == id_tarefa:
                tarefa_a_remover = tarefa
                break

        if tarefa_a_remover:
            lista_de_tarefas.remove(tarefa_a_remover)
            print(f"Tarefa com ID '{id_tarefa}' foi removida com sucesso!")
        else:
            print("ID da tarefa inválido! Tente novamente.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

def main():
    """
    Função principal que executa o programa de gerenciamento de tarefas.

    O programa exibe um menu de opções e permite ao usuário adicionar, 
    listar, marcar como concluída ou remover tarefas, além de sair do programa.
    O loop continua até que o usuário escolha a opção de sair (digite o número 0).
    
    Dentro do loop, o programa espera pela escolha do usuário e, com base na
    opção selecionada, executa a função correspondente:
    - Adicionar Tarefa: Chama a função para adicionar uma nova tarefa.
    - Listar Tarefas: Exibe a lista de tarefas pendentes.
    - Marcar Tarefa como Concluída: Permite ao usuário marcar uma tarefa como concluída.
    - Remover Tarefa: Remove uma tarefa da lista.
    - Sair: Encerra o programa com uma mensagem de despedida.

    O programa continua executando até que o usuário opte por sair, momento 
    em que a mensagem "Obrigado por usar o programa. Até logo!" é exibida.
    """
    lista_de_tarefas = []

    while True:
        exibir_menu()
        opcao_escolhida = obter_escolha()

        match opcao_escolhida:
            case 1: adicionar_tarefa(lista_de_tarefas)
            case 2: listar_tarefas(lista_de_tarefas)
            case 3: marcar_como_concluida(lista_de_tarefas)
            case 4: remover_tarefa(lista_de_tarefas)
            case 0:
                print("Obrigado por usar o programa. Até logo!")
                break
            case None: continue
            case _: print("Opção inválida! Tente novamente.")

main()
