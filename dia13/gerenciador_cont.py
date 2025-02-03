import csv

def adicionar_contato():
    nome = input("Nome:")
    telefone = input("Telefone: ")
    email=input("Email: ")

    with open('contatos.csv', 'a', newline = '') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow([nome, telefone, email])
    print("Contato adicionado com sucesso")
    
def listar_contatos():
    try:
        with open('contatos.csv', 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(f"Nome: {linha[0]}, Telefone: {linha[1]}, Email: {linha[2]}")
    except FileNotFoundError:
        print("Nenhum contato encontrado.")

while True:
    print("\nMenu:")
    print("1. Adicionar Contatos")
    print("2. Listar Contatos")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")        

    if opcao =='1':
        adicionar_contato()
    elif opcao == '2':
        listar_contatos()
    elif opcao == '3':
        break
    else:
        print("Opção inválida.")