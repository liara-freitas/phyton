try:
  arquivo = open('dados.txt', 'r')
  conteudo = arquivo.read()
except FileNotFoundError:
  print("Erro: O arquivo 'dados.txt' não foi encontrado")
else: 
  print("Arquivo lido com sucesso!")
  print(conteudo)
finally:
  print("Operação de leitura de arquivo finalizada.")