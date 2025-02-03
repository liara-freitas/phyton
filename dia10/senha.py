senha = input("Digite uma senha: ")

tem_maiuscula = any(c.isupper() for c in senha)
tem_minuscula = any(c.islower() for c in senha)
tem_numero = any(c.isdigit() for c in senha)
tem_simbolo = any(not c.isalnum() for c in senha)
tamanho_adequado = len(senha) >=8

if tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo and tamanho_adequado:
    print("Senha Forte!")
else:
    print("Senha fraca. Tente novamente.")