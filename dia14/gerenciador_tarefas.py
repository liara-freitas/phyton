import json
from multiprocessing import Value
import os
from datetime import datetime
import csv

def exportar_tarefas(tarefas):
    try:
        with open('tarefas_exportadas.csv', 'w', newline = '') as arquivo_csv:
            campos = ['ID', 'Título', 'Descrição', 'Data de Conclusão','Concluída']
            escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
            escritor.writeheader()
            for tarefa in tarefas:
                escritor.writerow({'ID': tarefa['id'],
                                  'Título': tarefa['titulo'],
                                  'Descrição': tarefa['descricao'],
                                  'Data de Conclusão': tarefa['data'],
                                  'Concluída': 'Sim' if tarefa['concluida'] else 'Não'}
                                  )
            print("Tarefas exportadas com sucesso para 'tarefas_exportadas.csv'.")
    except Exception as e:
        print(f"Ocorreu um erro ao exportar as tarefas{e}")
                
#Função para carregar as tarefas do arquivo
def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    else:
        return []

#Função para salvar as tarefas no arquivo
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

#Gerar ID para as tarefas
def gerar_id(tarefas):
    if tarefas:
        ultimo_id = tarefas[-1]['id']
        return ultimo_id + 1
    else:
        return 1
    
#Adicionar tarefa
def adicionar_tarefa(tarefas):
    print("\nAdicionar Nova Tarefa")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    data_input = input("Data de conclusão (dd/mm/aaaa): ")
    try:
        data_obj = datetime.strptime(data_input, '%d/%m/%Y')
        data = data_obj.strftime('%d/%m/%Y')
        if data_obj.date() < datetime.now().date():
            print("Data de conclusão não pode ser no passado.")
            return
    except ValueError:
        print("Data em formato inválido. Utilize dd/mm/aaaa.")
        return
    
    tarefa = {
        'id': gerar_id(tarefas),
        'titulo': titulo,
        'descricao': descricao,
        'data': data,
        'concluida':False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso")

#Listar Tarefas
def listar_tarefas(tarefas):
    print("\nTarefas Pendentes: ")
    tarefas_pendentes = [t for t in tarefas if not t['concluida']]
    tarefas_pendentes = sorted(tarefas_pendentes, key=lambda x:
    datetime.strptime(x['data'], '%d/%m/%Y'))
    for tarefa in tarefas_pendentes:
        data_obj = datetime.strptime(tarefa['data'], '%d/%m/%Y')
        status_atrasado = " [ATRASADA]" if data_obj.date() < datetime.now().date() else ""
        print(f"ID: {tarefa['id']} Título: {tarefa['titulo']}, Data: {tarefa['data']}{status_atrasado}")
    
    print("\n Tarefas Concluídas: ")
    tarefas_concluidas = [t for t in tarefas if t['concluida']]
    tarefas_concluidas = sorted(tarefas_concluidas, key=lambda x:
    datetime.strptime(x['data'], '%d/%m/%Y'))
    for tarefa in tarefas_concluidas:
        print(f"ID: {tarefa['id']} Título: {tarefa['titulo']}, Data: {tarefa['data']}")

  #Marcar a tarefa como concluida
def concluir_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa:  "))
        for tarefa in tarefas:
            if tarefa ['id'] == id_tarefa:
                if tarefa['concluida']:
                    print("A tarefa já está concluída.")
                else:
                    tarefa['concluida'] = True
                    salvar_tarefas(tarefas)
                    print("Tarefa concluída com sucesso!")
                    return
        print("Tarefa não encontrada.")
    except ValueError:
        print("ID inválido.")

#Remover tarefa
def remover_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa a ser removida: "))
        for tarefa in tarefas:
           if tarefa ['id'] == id_tarefa:
               tarefas.remove(tarefa)
               salvar_tarefas(tarefas)
               print("Tarefa removida com sucesso!")
               return
        print("Tarefa não encontrada.")
    except ValueError:
        print("ID inválido.")

#Pesquisar Tarefa
def pesquisar_tarefas(tarefas):
    termo = input("Digite o termo de pesquisa: ").lower()
    resultados = [t for t in tarefas if termo in t['titulo'].lower() or
                  termo in t['descricao'].lower()]
    if resultados:
        print(f"\nTarefas que contêm '{termo}': ")
        for tarefa in resultados:
            status = "Concluída" if tarefa ['concluida'] else "Pendente"
            print(f"ID: {tarefa['id']} Título: {tarefa['titulo']}, Status: {status}, Data: {tarefa['data']}")
    else:
       print("Nenhuma tarefa encontrada com o termo especificado.")

#Ordenar tarefa por data
def ordernar_tarefas(tarefas):
    tarefas.sort(key=lambda x: datetime.strptime(x['data'], '%d/%m/%Y'))
    salvar_tarefas(tarefas)
    print("Tarefas ordenadas por data de conclusão com sucesso!")

def editar_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa a ser editada: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                print(f"Editar a Tarefa ID {id_tarefa}:")
                novo_titulo = input(f"Novo Título (atual: {tarefa['titulo']}): ") or tarefa['titulo']
                nova_descricao = input (f"Nova Descrição (atual:{tarefa['descricao']}): ") or tarefa['descricao']
                nova_data = input(f"Nova Data de Conclusão (atual: {tarefa['data']}, formato dd/mm/aaaa): ") or tarefa['data']
                try:
                    data_obj = datetime.strptime(nova_data, '%d/%m/%Y')
                    if data_obj.date() < datetime.now().date():
                        print("Data de conclusão não pode ser no passado")
                        return
                    tarefa['data'] = data_obj.strftime('%d/%m/%Y')
                except ValueError:
                  print("Data em formato inválido. Utiliza dd/mm/aaaa")
                  return
                tarefa['titulo'] = novo_titulo
                tarefa['descricao'] = nova_descricao
                salvar_tarefas(tarefas)
                print("Tarefa editada com sucesso!")
                return
        print("Tarefa não encontrada.")
    except ValueError:
        print("ID inválido")   


#Menu principal
def menu():
    print("\n==== Gerenciador de Tarefas Avançado ====")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefa")
    print("3. Concluir Tarefa")
    print("4. Remover Tarefa")
    print("5. Pesquisar Tarefa")
    print("6. Ordenar Tarefa")
    print("7. Editar tarefa")
    print("8. Exportar Tarefas para CSV")
    print("9. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao


#Loop principal
def main():
    tarefas = carregar_tarefas()
    while True:
        opcao = menu()
        if opcao == '1':
          adicionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            remover_tarefa(tarefas)
        elif opcao == '5':
            pesquisar_tarefas(tarefas)
        elif opcao == '6':
            ordernar_tarefas(tarefas)
        elif opcao == '7':
            editar_tarefa(tarefas)
        elif opcao == '8':
            exportar_tarefas(tarefas)
        elif opcao == '9':
            print ("Encerramento do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
if __name__ == '__main__':
      main()

