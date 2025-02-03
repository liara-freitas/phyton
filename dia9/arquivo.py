import os

def manipular_arquivos():
    #Criando uma pasta
    os.mkdir('nova_pasta')
    print("Pasta 'nova_pasta' criada.")

    #Mudando para o novo diretório
    os.chdir('nova_pasta')

    #Criando um arquivo
    with open('arquivo.txt', 'w') as arquivo:
        arquivo.write("Este é um arquivo dentro da nova pasta")
    print("Arquivo 'arquivo.txt' criado dentro de 'nova_pasta'.")

    #Listando arquivos
    arquivos = os.listdir('.')
    print("Arquivos no diretório atual:", arquivos)

manipular_arquivos()