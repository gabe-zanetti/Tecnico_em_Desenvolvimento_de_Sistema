Nome=input("Qual é o nome do cliente?:")
Ingresso= int(input("1-Normal\n2-Estudante\n3-Idoso\nQual ingresso sera?:"))
preço=0

match Ingresso():
    case('1'):
        Preço=10
    case('2'):
        Preço=8
    case('3'):
        Preço=6
    case(_):
        print("Opção não existente")
        
def gerar_resumo():
    print=(Nome,"|", Ingresso,"|", preço)

gerar_resumo()
        