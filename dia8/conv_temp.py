def celsius_para_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def celsius_para_kevin(c):
    return c + 273.15

def kelvin_para_celcius(k):
    return k - 273.15

temperatura = float(input("Digite a temperatura: "))
unidade = input ("Digite a unidade atual (C, F, K): ").upper()
converter_para = input("Converter para (C, F, K): ").upper()

if unidade == "C":
      if converter_para == "F":
          resultado = celsius_para_fahrenheit(temperatura)
      elif converter_para == "K":
          resultado = celsius_para_kevin(temperatura)
elif unidade == "F":
      if converter_para == "C":
           resultado = fahrenheit_para_celsius(temperatura)
      elif converter_para =="K":
           celsius = fahrenheit_para_celsius(temperatura)
           resultado  = celsius_para_kevin(celsius)
elif unidade == "K":
      if converter_para =="C": 
       celsius = fahrenheit_para_celsius(temperatura)
      elif converter_para == "F":
          celsius = kelvin_para_celcius(temperatura)
          resultado = celsius_para_fahrenheit(celsius)
else:
    resultado = "Unidade inválida."

print (f"Temperatura convertida: {resultado} {converter_para}")
