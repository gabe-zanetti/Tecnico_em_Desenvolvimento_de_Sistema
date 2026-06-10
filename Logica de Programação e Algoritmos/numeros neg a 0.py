numeros=[]

for i in range(0,6):
    numero=int(input("Qual é o numero? "))
    numeros.append(numero)

for i in range(0,6):
        if (numero[i]<0):
            numero[i]=0
            print("O numero é negativo:", numero[i])

print(numeros)
