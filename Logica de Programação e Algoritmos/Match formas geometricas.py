#Match case
print("===Opções de formas geometricas===\n1-Quadrado \n2-Circulo \n3-Triangulo")
Forma_Geometrica=int(input("Digite o numero corespondente a uma forma geometrica: "))

match Forma_Geometrica:
    case '1':
        Print("⬜⬛")
    case '2':
        print("🟠🔵")
    case '3':
        print("🔺🔻")
    case _:
        print("POR FAVOR digite uma opção valida (⓿_⓿)")