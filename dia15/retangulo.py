class Retangulo:
  def __init__(self, largura, altura):
    self.largura = largura
    self.altura = altura

  def area(self):
    return self.largura * self.largura
    
  def perimetro(self):
    return 2 * (self.largura + self.altura)
    
retangulo = Retangulo(5, 3)
print(f"Área: {retangulo.area()}")
print(f"Perímetro: {retangulo.perimetro()}")