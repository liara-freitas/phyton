import json
import os
from datetime import datetime
import logging


#Configurar Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s ')

#Definindo classes prinicipais
class Livro:
  def __init__(self, id, titulo, autor, ano, isbn,disponivel):
    self.id = id
    self.titulo = titulo
    self.autor = autor
    self.ano = ano
    self.isbn = isbn
    self.disponivel = True

  def exibir_informacoes(self):
    status = "Disponível" if self.disponivel else "Emprestado"
    print (f"ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, ISBN: {self.isbn}, Status: {status} ")


class Usuario:
  def __init__(self, id, nome, email, telefone):
    self.id = id
    self.nome = nome
    self.email = email
    self.telefone = telefone

  def exibir_informacoes(self):
    print(f"ID: {self.id}, Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}") 

class Emprestimo:
  def __init__(self, id, usuario_id, livro_id, data_emprestimo, data_devolucao=None):
    self.id = id
    self.usuario_id = usuario_id
    self.livro_id = livro_id
    self.data_emprestimo = data_emprestimo
    self.data_devolucao = data_devolucao

  def exibir_informacoes(self):
    status = "Devolvido" if self.data_devolucao else "Pendente"
    print(f"ID: {self.id}, Usuario ID: {self.usuario_id}, Livro ID: {self.livro_id}, Data Empréstimo: {self.data_emprestimo}, Data Devolução: {self.data_devolucao}, Status: {status}")

#Funções para Carregar e Salvar Dados
def carregar_dados(nome_arquivo):
  if os.path.exists(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
      return json.load(arquivo)
  else:
    return []

def salvar_dados(nome_arquivo, dados):
  with open(nome_arquivo, 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)

#Funções para Gerenciamento de Livros
def cadastrar_livro(livros):
  id = len(livros) + 1
  titulo = input("Título do Livro: ").strip()
  if not titulo:
    print("Título não pode ser vazio.")
    return


  autor = input("Autor: ").strip
  if not autor:
    print("Autor não pode ser vazio.")
    return
  
  ano = input("Ano de Publicação: ").strip()
  if not ano.isdigit() or int(ano) <=0:
    print("Ano de publicação inválido.")

  isbn = input("ISBN: ").strip()
  if not isbn:
    print("ISBN não pode ser vazio.")
    return



  livro = Livro(id, titulo, autor, ano, isbn)
  livros.append(livro.__dict__)
  salvar_dados('livros.json', livros)
  logging.info(f"O livro '{titulo}' cadastrado com sucesso")

def listar_livros(livros):
  print("\n=== Lista de Livros ===")
  for livro_dict in livros:
      livro = Livro(**livro_dict)
      livro.exibir_informacoes()

#Gerenciamento de Usuários
def cadastrar_usuario(usuarios):
  id = len(usuarios) + 1
  nome = input("Nome do Usuário: ").strip()
  if not nome:
    print("Nome não pode ser vazio.")
    return
  
  email = input("Email: ").strip()
  if "@" not in email or "." not in email:
    print("Email inválido.")

  telefone = input("Telefone: ").strip()
  if not telefone.isdigit() or len(telefone) < 10:
    print("Telefone inválido. Deve conter pelo menos 10 dígitos.")

  usuario = Usuario(id, nome, email, telefone)
  usuarios.append(usuario.__dict__)
  salvar_dados('usuarios.json', usuarios)
  logging.info(f"Usuário '{nome}' cadastrado com sucesso. ")

def listar_usuarios(usuarios):
  print("\n=== Lista de Usuários ===")
  for usuario_dict in usuarios:
    usuario = Usuario(**usuario_dict)
    usuario.exibir_informacoes()

#Gerencimento de empréstimos
def emprestar_livro(emprestimos, livros, usuarios):
    id = len(emprestimos) + 1
    usuario_id = int(input("ID do usuário: "))
    livro_id = int(input("ID do Livro: "))

    #Verificar se o usuário existe
    usuario_existente = any(u['id'] == usuario_id for u in usuarios)
    if not usuario_existente:
      print("Usuário não encontrado.")
      return
    
    #Verificar livro disponível
    livro = next((l for l in livros if l ['id'] == livro_id), None)
    if not livro:
      print("Livro não encontrado")
      return
    
    if not livro['disponivel']:
      print("Livro não está disponível para empréstimo")
      return
    
    data_emprestimo  = datetime.now().strftime('%d/%m/%Y')
    emprestimo = Emprestimo(id, usuario_id, livro_id, data_emprestimo)
    emprestimos.append(emprestimo.__dict__)

    #Atualizar disponibilidade do livro
    livro['disponivel'] = False

    salvar_dados('emprestimo.json', emprestimos)
    salvar_dados('livros.json', livros)
    logging.info(f"Livro ID {livro_id} emprestado para Usuário ID {usuario_id}.")

def devolver_livro(emprestimos, livros):
  id_emprestimo = int(input("ID do Empréstimo: "))
  emprestimo = next((e for e in emprestimos if e['id'] == id_emprestimo), None)

  if not emprestimo:
    print("Empréstimo não encontrado.")
    return
  if emprestimo['data_devolucao']:
    print ("Livro já foi devolvido.")
    return
  
  data_devolucao = datetime.now().strftime('%d/%m/%Y')
  emprestimo['data_devolucao'] = data_devolucao

  #Atualizar disponibilidade do livro
  livro_id = emprestimo['livro_id']
  livro = next((l for l in livros if ['id'] == livro_id), None)
  if livro:
    livro['disponivel'] = True
  
  salvar_dados('emprestimo.json', emprestimos)
  salvar_dados('livros.json', livros)
  logging.info(f"Livro ID {livro_id} devolvido pelo Usuário ID {emprestimo['usuario_id']}.")

def listar_emprestimos(emprestimos):
  print("\n=== Lista de Empréstimos ===")
  for emprestimo_dict in  emprestimos:
    emprestimo = Emprestimo(**emprestimo_dict)
    emprestimo.exibir_informacoes()

#Funções de Pesquisa
def pesquisar_livros(livros):
  termo = input("Digite o termo de pesquisa para o livro: ").lower()
  resultados = [l for l in livros if termo in l ['titulo'].lower() or termo in l ['autor'].lower()]
  if resultados:
    print(f"\n=== Resultados da Pesquisa por Livros: '{termo}' ====")
    for livro_dict in resultados:
      livro = Livro(**livro_dict)
      livro.exibir_informacoes()    
  else:
    print("Nenhum livro encontrado com o termo especificado")

def pesquisar_usuarios(usuarios):
  termo = input("Digite o termo de pesquisa para usuários: ").lower()
  resultados = [u for u in usuarios if termo in u['nome'].lower() or termo in u ['email'].lower()]
  if resultados:
    print(f"\n=== Resultados da Pesquisa por Usuários: '{termo}' ===")
    for usuario_dict in resultados:
      usuario = Usuario(**usuario_dict)
      usuario.exibir_informacoes()
  else:
    print("Nenhum usuário encontrado com o termo especificado.")

#Gerar relatóris
def gerar_relatorio_emprestimo(emprestimos, usuarios, livros):
  print("\n=== Relatórios de Empréstimos ===")
  for emprestimo_dict in emprestimos:
    emprestimo = Emprestimo(**emprestimo_dict)
    usuario = next((u for u in usuarios if u ['id'] == emprestimo.usuario_id), None)
    livro = next((l for l in livros if l ['id'] == emprestimo.livro_id), None)
    if usuario and livro:
      status = 'Devolvido' if emprestimo.data_devolucao else "Pendentes"
      print(f"Empréstimo ID: {emprestimo.id}, Usuário: {usuario['nome']}, Livro: {livro['titulo']}, Data Empréstimo: {emprestimo.data_emprestimo}, Data Devolução: {emprestimo.data_devolucao}, Status: {status}")

def atualizar_livro(livros):
  id_livro = int((input("Digite o ID do livro a ser atualizado: ")))
  livro = next((l for l in livros if l ['id'] == id_livro), None)
  if not livro:
    print("Livro não encontrado")
    return
  
  print(f"Atualizando Livro ID {id_livro}: ")
  novo_titulo = input(f"Novo Título (atual: {livro['titulo']}): ") or livro['titulo']
  novo_autor = input(f"Novo Autor (atual: {livro['autor']}): ") or livro['autor']
  novo_ano = input(f"Novo ano de publicação (atual: {livro['ano']}): ") or livro['ano']
  novo_isbn = input(f"Novo ISBN (atual: {livro['isbn']}): ") or livro['isbn']

  livro['titulo'] = novo_titulo
  livro['autor'] = novo_autor
  livro['ano'] = novo_ano
  livro['isbn'] = novo_isbn

  salvar_dados('livro.json', livros)
  logging.info(f"Livro ID {id_livro} atualizando com sucesso")

def atualizar_usuario(usuarios):
  id_usuario = int(input("Digite o ID do usuário a ser atualizado: "))
  usuario = next((u for u in usuarios if u ['id'] == id_usuario), None)
  if not usuario:
    print("Usuário não encontrado")
    return
  
  print(f"Atualizando Usuário ID {id_usuario}: ")
  novo_nome = input(f"Novo Nome (atual: {usuario['nome']}): ") or usuario['nome']
  novo_email = input(f"Novo Email (atual: {usuario['email']}): ") or usuario['email']
  novo_telefone = input(f"Novo Telefone (atual: {usuario['telefone']}): ") or usuario['telefone']

  usuario['nome'] = novo_nome
  usuario['email'] = novo_email
  usuario['telefone'] = novo_telefone

  salvar_dados('usuarios.json', usuarios)
  logging.info(f"Usuário ID {id_usuario} atualizado com sucesso. ")


#Menu Principal
def menu():
  print("\n=== Sistema de Gerenciamento de Biblioteca ===")
  print("1. Cadastrar Livro")
  print("2. Listar Livro")
  print("3. Cadastrar Usuário")
  print("4. Listar Usuário")
  print("5. Emprestar Livro")
  print("6. Devolver Livro")
  print("7. Listar Empréstimo")
  print("8. Pesquisar Livros")
  print("9. Pesquisar Usuários")
  print("10. Gerar Relatório de Empréstimos")
  print("11. Atualizar Livro")
  print("12. Atualizar Usuário")
  print("13. Sair")
  opcao = input("Escolha uma opcao: ")
  return opcao

def main():
  #Carregar dados
  livros = carregar_dados('livros.json')
  usuarios = carregar_dados('usuarios.json')
  emprestimos = carregar_dados('emprestimo.json')

  while True:
    opcao = menu()
    if opcao == '1':
      cadastrar_livro(livros)
    elif opcao == '2':
      listar_livros(livros)
    elif opcao == '3':
      cadastrar_usuario(usuarios)
    elif opcao == '4':
      listar_usuarios(usuarios)
    elif opcao == '5':
      emprestar_livro(emprestimos, livros, usuarios)
    elif opcao == '6':
      devolver_livro(emprestimos, livros)
    elif opcao == '7':
      listar_emprestimos(emprestimos)
    elif opcao == '8':
      pesquisar_livros(livros)
    elif opcao == '9':
      pesquisar_usuarios(usuarios)
    elif opcao == '10':
      gerar_relatorio_emprestimo(emprestimos, usuarios, livros)
    elif opcao == '11':
      atualizar_livro(livros)
    elif opcao == '12':
      atualizar_usuario(usuarios)
    elif opcao == '13':
      print("Encerrando o sistema de biblioteca. Até mais!")
      break
    else:
      print("Opção inválida. Por favor, escolhar uma opção válida.")


if __name__ == '__main__':
  main()