numeros=[]
media=0
soma=0
for i in range(6):
    num = int(input("Digite um número:"))
    numeros.append(num)
for num in numeros:
    soma= soma+num
media= soma/6
print(media)