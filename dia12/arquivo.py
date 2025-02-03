def ler_arquivo(nome_arquivo):
  try:
    with open(nome_arquivo, 'r') as arquivo:
      conteudo = arquivo.read()
      print(conteudo)
  except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
  except PermissionError:
      print("Erro: Permisão negada para ler o arquivo.")
  except Exception as e:
    print (f"Ocorreu um erro inesperado: {e}")

ler_arquivo('dados.txt')