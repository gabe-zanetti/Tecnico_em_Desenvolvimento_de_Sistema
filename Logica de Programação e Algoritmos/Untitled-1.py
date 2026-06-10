preço=float(input("Qual é o preço do café?"))
quantidade=int(input("Qual é a quantidade que foi vendido"))
Total=0
def Calcular_Total():
    Total=preço*quantidade
    print("O total a ser pago sera", Total)
Calcular_Total()


