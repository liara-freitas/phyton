class Cachorro:
  def __init__(self, nome,idade):
    self.nome = nome
    self.idade = idade

  def latir(self):
    print(f"{self.nome} está latindo!")

  def aniversario(self):
    self.idade +=1

dog = Cachorro("Rex", 5)
dog.latir()
print(f"Idade: {dog.idade}")
dog.aniversario()
print(f"Nova idade: {dog.idade}")