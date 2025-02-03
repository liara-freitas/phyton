tarefas = []

while True:
    print("\nMenu de Tarefas: ")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefa")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao =="1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso.")
    elif opcao == "2":
      tarefa = input("Digite a tarefa a ser removida: ")
      if tarefa in tarefas:
         tarefas.remove(tarefa)
         print("Tarefa removida.")
    elif opcao ==  "3":
        print("\nLista de Tarefas:")
        for idx, tarefa in enumerate(tarefas, start =1):
           print(f"{idx}. {tarefa}")
    elif opcao == "4":
       print("Saindo do programa.")
       break
    else:print("Opção inváçida. Tente novamente.")
