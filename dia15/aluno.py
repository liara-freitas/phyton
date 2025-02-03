class Aluno:
  def __init__(self, nome):
    self.nome  = nome
    self.notas = []
    
  def adicionar_nota(self, nota):
    self.notas.append(nota)

  def calcular_media(self):
    if self.notas:
      return sum(self.notas) / len(self.notas)
    
    else:
      return 0 
    
aluno = Aluno("João")
aluno.adicionar_nota(8.5)
aluno.adicionar_nota(7.0)
aluno.adicionar_nota(9.0)

media = aluno.calcular_media()

print(f"Média de {aluno.nome}: {media: .2f}")


