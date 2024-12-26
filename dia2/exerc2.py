from xmlrpc.client import boolean


nome = "Liara"
idade = 23
altura = 1.55
estudante = True
maior_de_idade = boolean

print("Nome:", nome)
print("Idade:", idade)
print("altura:", altura)
print("Estudante:" , estudante)

ano_nascimento = 2024 - idade

print("Ano de Nascimento", ano_nascimento)

maior_de_idade = idade >= 18

print("Maior de Idade:", maior_de_idade)

frase = "Olá, meu nome é " + nome + " e eu tenho " + str(idade) + " anos."

print(frase)