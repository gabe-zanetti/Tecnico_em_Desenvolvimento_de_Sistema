numeros=[]
numero=0
for i in range(8):
    num =int(input("Quais são os números?"))
    numeros.append(num)

numero=int(input("Digite um número para poder buscar"))

for i in range(8):

    if(numeros[i]==numero):
        print("Esse número esta presente")