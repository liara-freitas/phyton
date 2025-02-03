class Observador:
  def atualizar(self, mensagem):
    pass

class Aluno(Observador):
  def __init__(self, nome):
    self.nome = nome

  def atualizar(self, mensagem):
      print(f"{self.nome} recebeu a mensagem: {mensagem}")

class Professor:
  def __init__(self):
    self.observadores = []

  def adicionar_observador(self, observador):
      self.observadores.append(observador)

  def remover_observador(self, observador):
     self.observadores.remove(observador)

  def notificar_observadores(self, mensagem):
      for observador in self.observadores:
        observador.atualizar(mensagem)

professor = Professor()
aluno1 = Aluno("Ana")
aluno2 = Aluno("Pedro")
professor.adicionar_observador(aluno1)
professor.adicionar_observador(aluno2)

professor.notificar_observadores("A aula será amanhã ás 16:00")