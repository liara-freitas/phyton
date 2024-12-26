senha_inserida = "abcd1234"
senha_correta = "abcd1234"
user_bloq = False

#Verificar o acesso

acesso_concedido = (senha_inserida == senha_correta) and not user_bloq

print("Acesso concedido? ", acesso_concedido)