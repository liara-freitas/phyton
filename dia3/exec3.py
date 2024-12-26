from numpy import true_divide


idade = 23
carteira_hab = True

#Verifica se pode alugar um carro

pode_alugar = (idade>=21) and carteira_hab
print("Pode alugar o carro? ", pode_alugar )

#Verifica se tem direito a meia entrada

estudante = False
idoso = idade >= 60
meia_entrada = estudante or idoso

print("Tem direito a meia entrada? ", meia_entrada)

#Inverter uma condição
chovendo = False
nao_chovendo = not chovendo
print ("Está chovendo? ", chovendo) #False
print ("Não está chovendo? ", nao_chovendo) # True
