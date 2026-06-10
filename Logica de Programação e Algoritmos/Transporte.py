Opção=input("Aplicativo de transporte \nOpções de corrida: \n1-Economica \n2-Conforto \n 3-Luxo \nQual opção deseja usar?: ")
match Opção:
    case(1):
        print("Opção economica selecionada")
    case(2):
        print("Opção Conforto selecionada")
    case(1):
        print("Opção Luxo selecionada")
    case _:
        print("Opção não existente")
    