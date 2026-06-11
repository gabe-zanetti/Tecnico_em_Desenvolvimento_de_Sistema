#Importando tempo, sistema operacional e o sistema. É necessario para certas funções funcionarem
import time
import os
import sys

produtos=[] #Array aonde os produtos irão ser armazenados
opcao_inicial=0 #Não é possivel usar uma variavel em um while se ela não for criada antes

def limpar(): #Função criada com o proposito de não precisar escrever esses codigos denovo e denovo
    input("Aperte 'enter' para voltar ao menu: ") #Para não apagar a tela sem o usuario pedir
    os.system('cls') #Para limpar a tela do terminal


while opcao_inicial!=4: #O codigo ira rodas até a opção 4 for selecionada
    print("""                                                               
  ,---.                      ,--.,--.                          
 /  O  \  ,---. ,---.  ,---. |  |`--',--,--,--. ,---.  ,--,--. 
|  .-.  || .--'| .-. :(  .-' |  |,--.|        || .-. |' ,-.  | 
|  | |  |\ `--.\   --..-'  `)|  ||  ||  |  |  || '-' '\ '-'  | 
`--' `--' `---' `----'`----' `--'`--'`--`--`--'|  |-'  `--`--' 
                                               `--'            '
                                               """)
    print("Olá e bem vindo ao programa de produtos de limpeza da Aceslimpa!\n1-Cadrasta produto\n2-Mostrar produto\n3-Escluir produto\n4-Sair")
    opcao_inicial=input("Como podemos te ajudar?:")

    match opcao_inicial: #Para rodar as opções
        case '1':
            print("Entendido! Vamos mostrar as zonas de cadastro!")
            nome_produto=input("Qual é o nome do produto?: ")
            preco_por_produto=input("Qual é o preço do produto?:")
            descricao=input("Qual a descrição do produto?: ")

            produto={ #Colocando as respostas em um JSON
                'nome': nome_produto,
                'preco_por_produto': preco_por_produto,
                'descricao': descricao
            }

            produtos.append(produto) #Salvando no array
            print("Produto salvo!")
            limpar() #Chamando função

        case '2':
            print("Entendido! Iremos te mostrar os produtos ja cadastrados")

            if(len(produtos)==0): #Ver se tem algum produto cadastrado
                print("Nenhum produto ainda foi cadastrado")

            else: #Se tiver sera mostrado todos os produtos salvos
                for produto in produtos:
                    print("------- \n", produto["nome"], "\n")
                    print(produto["preco_por_produto"], "\n")
                    print(produto["descricao"], "\n")

            limpar()

        case '3':
            para_encontrar=input("Qual produto gostaria que nos excluimos?: ")
            encontrado=False

            for produto in produtos: #Para encontrar e excluir o produto
                if (produto['nome']==para_encontrar):
                    produtos.remove(produto)
                    encontrado=True
                    print("Produto removido com sucesso!")

            if (encontrado==False): #Se não existir
                    print("Produto não existe")
            limpar()

        case '4':
            print("Te vemos na proxima! ^^")
            time.sleep(5) #O programa esperara 5 segundos e depois fechara 
            sys.exit()

        case _: #Case reservado para erros de usuario
            print("Opção não existe :(")

            limpar()#Chamando função
