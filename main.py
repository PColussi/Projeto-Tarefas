def adicionar_tarefas(tarefas):
    nome = input("Digite o nome da tarefa a ser adicionada: ")
    descricao = input('Digite a descrição da tarefa: ')
    while True:
        prioridade = int(input("Prioridade da tarefa (de 1 a 5): "))
        if 1 <= prioridade <= 5:
            break
        else:
            print("Por favor, insira um valor de prioridade válido (de 1 a 5).")
    categoria = input("Categoria da tarefa: ")

    tarefa = {"nome": nome, "descricao": descricao, "prioridade": prioridade, "categoria": categoria, "concluida": False}

    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso.")


def listar_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas cadastradas.")
    else:
        for i, tarefa in enumerate(tarefas):
            print(f"Tarefa: {i+1}: ")
            print(f"Nome: {tarefa['nome']}")
            print(f"Descrição: {tarefa['descricao']}")
            print(f"Prioridade: {tarefa['prioridade']}")
            print(f"Categoria: {tarefa['categoria']}")
            print()

def marcar_concluida(tarefas):
    if not tarefas:
        print("Não existe tarefas.")
    else:
        listar_tarefa(tarefas)
        num_tarefa = int(input("Digite o número da tarefa a ser concluída: "))
        num_tarefa -= 1
        if 0<=num_tarefa < len(tarefas):
            tarefas[num_tarefa]["concluida"] = True
            print("Tarefa marcada como concluída.")
        else:
            print("Número de tarefa inválido.")


def prioridade_alta(tarefas):
    while True:
        prioridade_desejada = int(input("Digite a prioridade desejada (1-5): "))
        if 1 <= prioridade_desejada <= 5:
            break
        else:
            print("Por favor, insira um valor de prioridade válido (de 1 a 5).")
    print(f"Tarefas com prioridade {prioridade_desejada}:")
    for tarefa in tarefas:
        if tarefa["prioridade"] == prioridade_desejada:
            print(f"{tarefa['nome']}: {tarefa['descricao']}")


def exibir_categoria(tarefas):
    categoria_desejada = input("Digite a categoria desajada: ")
    tarefas_encontradas = False
    print(f"Tarefas na categoria {categoria_desejada}:")
    for tarefa in tarefas:
        if tarefa['categoria'] == categoria_desejada:
            print(f"{tarefa['nome']}: {tarefa['descricao']}")
            tarefas_encontradas = True
        if not tarefas_encontradas:
            print("Não há tarefas nessa categoria.")



def menu():
    tarefas = []

    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Exibir tarefas por prioridade")
        print("5. Exibir tarefas por categoria")
        print("6. Sair")

    
        opcao = int(input("Digite a opção que você deseja: "))

        if opcao == 1:
            adicionar_tarefas(tarefas)
        elif opcao == 2:
            listar_tarefa(tarefas)
        elif opcao == 3:
            marcar_concluida(tarefas)
        elif opcao == 4:
            prioridade_alta(tarefas)
        elif opcao == 5:
            exibir_categoria(tarefas)
        elif opcao == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


menu()
