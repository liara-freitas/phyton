from abc import ABC, abstractmethod

class Veiculo(ABC):
  @abstractmethod
  def mover(self):
    pass

class Carro(Veiculo):
  def mover(self):
    print("O carro está se movendo")

class Moto(Veiculo):
  def mover(self):
        print("A moto está se movendo")

class FabricaVeiculos:
   def criar_veiculo(self, tipo):
      if tipo == "carro":
         return Carro()
      elif tipo == "moto":
         return Moto()
      else:
         raise ValueError("Tipo de veículo desconhecido.")

fabrica = FabricaVeiculos()
carro = fabrica.criar_veiculo("carro")
moto = fabrica.criar_veiculo("moto")

carro.mover()
moto.mover()