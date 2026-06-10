medicamentos=[]
for i in range(0,5):
    nome=input("Escreva o nome: ")
    fabricante=input("Escreva o fabricante: ")
    quantidade=int(input("Dgitie a quantidade: "))
    preco=float(input("Escreva o preço: "))

    medicamento={
        'Nome': nome,
        'Fabricante': fabricante,
        'Quantidade': quantidade,
        'Preço': preco
    }

    medicamentos.append(medicamento)

for medicamento in medicamentos:
    if (medicamento[quantidade] <10 ):
        print(medicamento[nome])