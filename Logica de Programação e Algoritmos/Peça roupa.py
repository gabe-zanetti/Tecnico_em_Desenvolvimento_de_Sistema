Nome=input("Qual é o nome da peça de roupa?:")
Preço=float(input("Qual é o preço da peça de roupa?:"))

def Aplicar_desconto(Preço):
    Desconto=Preço/20
    Com_desconto=Preço-Desconto
    print(Nome,"|", Com_desconto)

Aplicar_desconto(Preço)
