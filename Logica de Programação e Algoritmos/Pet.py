Nome_pet=input("Qual é o nome do Animal de estimação?:")
Especies=input("Qual é a especies do animal?:")
Idade=int(input("Qual é a idade do animal?:"))
Nome_dono=input("Qual é o nome do dono?:")

Pet={
    'Nome_pet': Nome_pet,
    'Especie': Especies,
    'Idade': Idade,
    'Nome_dono': Nome_dono
}
print(Pet['Nome_pet'])
print(Pet['Especie'])
print(Pet['Idade'])
print(Pet['Nome_dono'])