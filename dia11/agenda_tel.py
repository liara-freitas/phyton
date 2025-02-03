agenda = {}

def adicionar_contato ():
    nome = input ("Nome: ")
    telefone = input("Telefone: ")
    agenda[nome] = telefone
    print("Contato adicionado com sucesso")

def buscar_contato():
    nome = input("Nome do contato a buscar: ")
    if nome in agenda:
        print(f"Telefone de {nome}: {agenda[nome]}")
    else:
        print("Contato não encontrado.")

def remover_contato():
    nome  = input ("Nome do contato a remover: ")
    if nome in agenda:
        del agenda[nome]
        print("Contato removido com sucesso!")
    else:
        print("Contato não encontrado.")

while True:
    print("\n1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Remover contato")
    print("4. Sair")
    opcao = input ("Escolha uma opção: ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        buscar_contato()
    elif opcao == "3":
        remover_contato()
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")