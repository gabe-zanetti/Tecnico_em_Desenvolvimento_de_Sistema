#Sistema de cadastro de usuarios e produtos
#O sistema devera permitir
#-cadastrar
#-listar
#-deletar

#Criação das listas

Usuarios =[]
Produtos = []
#Funções
def Menu_Usuarios():
    Opção_menu_usuario=0

    while(Opção_menu_usuario !=4):
        print("---Menus de usuarios---\n1-Cadastrar usuario\n2-listar usuarios\n3-deletar usuarios\n4-Sair")
        Opção_menu_usuario=int(input("Escolha uma opção: "))
        match Opção_menu_usuario:

            #Cadastrar usuario
            case 1:
                Nome=input("Escreva o nome: ")
                Telefone=input("Escreva o telefone: ")
                E_mail=input("Escreva o email: ")

                #Criação do Json
                usuario= {
                    'Nome': Nome,
                    'Telefone': Telefone,
                    'Email': E_mail
                }

                #Adicionando no array
                Usuarios.append(usuario)
                print(f"usuario {usuario["Nome"]} cadastrado com sucesso")

            #Listar usuario
            case 2:
                print("\nlista de usuarios")

                if(len(Usuarios)==0):
                    print("Nenhum usuario cadastrado")

                else:
                    for usuario in Usuarios:
                        print("------\n usuario= ", usuario["Nome"])
                        print("\ntelefone= ", usuario["Telefone"])
                        print("\nemail= ", usuario["Email"])

            #Deletar usuario
            case 3:
                Nome_Deletar=input("Digite o nome do usuario que deseja deletar: ")
                encontrado= False 

                for usuario in Usuarios:
                    if (usuario["Nome"]== Nome_Deletar):
                        Usuarios.remove(usuario)
                        encontrado==True
                        print("Usuario removido com sucesso")

                if (encontrado==False):
                    print("Usuario não existente")
            #Sair
            case 4:
                break

            case _:
                print("Opção invalida")

#Produtos
def Menu_Produtos():
    Opção_menu_produtos=0

    while(Opção_menu_produtos !=5):
        print("---Menus deprodutos---\n1-Cadastrar produtos\n2-listar produtos\n3-deletar produtos\n4-Calcular produtos\n5-Sair")
        Opção_menu_usuario=int(input("Escolha uma opção: "))
        match Opção_menu_produtos:

            #Cadastrar usuario
            case 1:
                Nome=input("Escreva o nome: ")
                Descrição=input("Escreva a descrição: ")
                Quantidade=float(input("Escreva a quantidade: "))
                Valor=float(input("Escreva o valor: "))

                #Criação do Json
                produto= {
                    'Nome': Nome,
                    'Descrição': Descrição,
                    'Quantidade': Quantidade,
                    'valor': Valor
                }

                #Adicionando no array
                produtos.append(produto)
                print(f"produto {produto["Nome"]} cadastrado com sucesso")

            #Listar usuario
            case 2:
                print("\nlista de produtos")

                if(len(Produtos)==0):
                    print("Nenhum produto cadastrado")

                else:
                    for produto in Produtos:
                        print("------\n Nome= ", produto["Nome"])
                        print("\nDescrição= ", produto["Descrição"])
                        print("\nQuantidade= ", produto["Quantidade"])
                        print("\nValor= ", produto["Valor"])

            #Deletar usuario
            case 3:
                Nome_Deletar=input("Digite o nome do produto que deseja deletar: ")
                encontrado= False 

                for produto in Produtos:
                    if (produto["Nome"]== Nome_Deletar):
                        produto.remove(Produtos)
                        encontrado==True
                        print("Usuario removido com sucesso")

                if (encontrado==False):
                    print("Usuario não existente")
            #Calcular preço produtos
            case 4:
                print("Não deu tempo")

            #Sair
            case 5:
                break

            case _:
                print("Opção invalida")


#Menu principal

Opção_menu=0
while(Opção_menu != 3):
    print("---Menu de cadastro---\n Opções:\n1-usuarios\n2-produtos\n3-sair")
    Opção_menu=int(input("Escolha uma opção: "))


#Para fazer as opções
    match Opção_menu:

        case 1:
            Menu_Usuarios()

        case 2:
           Menu_Produtos()

        case 3:
            print("Ate logo")

        case _:
            print("Opção invalida")