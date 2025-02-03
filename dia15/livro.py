class Livro:
  def __init__(self, titulo, autor, ano):
    self.titulo = titulo
    self.autor = autor
    self.ano = ano

  def exibir_informacoes(self):
    print(f"Título: {self.titulo}")
    print(f"Autor: {self.autor}")
    print(f"Ano: {self.ano}")

livro = Livro("1984", "George Orwell", 1949)
livro.exibir_informacoes
