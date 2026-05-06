lado1=float(input("Digite o número do primeiro lado"))
lado2=float(input("Digite o número do segundo lado"))
lado3=float(input("Digite o número do terceiro lado"))

if(lado1+lado2>lado3 or lado1+lado2>lado2 or lado2+lado3>lado1):
    if (lado1==lado2 and lado1==lado3 and lado2==lado3):
         print("O triangulo é equilátero")
    elif (lado1!=lado2 and lado2 !=lado3 and lado1 != lado3):
        print("O triangulo é escaleno")
    else:
        print("O triangulo é escaleno")
else:
    print("Triangulo invalido")