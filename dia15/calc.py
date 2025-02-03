class Calculadora:
      def somar(self, a, b):
            return a + b
      
      def subtrair(self, a, b):
            return a - b
      
      def multiplicar(self, a, b):
            return a * b
      
      def dividir(self, a, b):
          if b != 0:
            return a / b
          
          else: 
              print("Erro: Divisão por zero.")
              return None
          
calc = Calculadora()
print(calc.somar(5, 3))
print(calc.subtrair(5, 3))
print(calc.multiplicar(5, 3))
print(calc.dividir(5, 0))


