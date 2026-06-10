nome=input("Qual e o nome do produto?:")
preco=float(input("Qual e o nome do produto?:"))
garantia=int(input("1-sem garantia\n2-garantia de 1 ano\n2-garantia de 2 anos\n Qual e a garantia do produto?:"))
extra=0

def preco_com_garantia(preco, extra):
    preco_com_garantia2
    preco_com_garantia2=preco-(preco/extra)
    print(preco_com_garantia2)
match garantia():
    case(1):
        extra=0
    case(2):
        extra=8
    case(3):
        extra=15
    case(_):
        print("Opção não existente")
    
preco_com_garantia(preco, extra)