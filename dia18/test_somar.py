def somar(a, b):
  return a + b

def test_somar_positivos():
  assert somar(2, 3) == 5

def test_somar_negativos():
  assert somar(-1, -1) == -2

def test_somar_zero():
  assert somar (0,5) == 5