import conversoes

temperatura_c = float(input("Digite a temperatura em Celsius: "))
temperatura_f = conversoes.celsius_para_fahrenheit(temperatura_c)
temperatura_k = conversoes.celsius_para_kelvin(temperatura_c)

print(f"{temperatura_c}°C equivalem a {temperatura_f}°F e {temperatura_k}K")