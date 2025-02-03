class UsuarioNaoEncontradoError(Exception):
  pass
class SenhaIncorretaError(Exception):
  pass
usuarios = {
'admin': '1234',
'usuario1': 'senha1'
}
def login():
  try:
    nome_usuario = input("Nome de usuário: ")
    senha = input("Senha: ")
    if nome_usuario not in usuarios:
      raise UsuarioNaoEncontradoError("Usuário não encontrado.")
    elif usuarios[nome_usuario] != senha:
      raise SenhaIncorretaError("Senha incorreta.")
  except UsuarioNaoEncontradoError as e:
    print(f"Erro: {e}")
  except SenhaIncorretaError as e:
    print(f"Erro: {e}")
  else:
    print("Login realizado com sucesso.")

login()