Nome=input("Qual é o nome da bebida")
preço=float(input("Qual é o preço da bebida?"))
quantidade=int(input("Qual é a quantidade que foi vendido"))
Total=0
print(Nome,"|", preço,"|",quantidade)
def Calcular_Total():
    Total=preço*quantidade
    print("O total a ser pago sera", Total)
Calcular_Total()


