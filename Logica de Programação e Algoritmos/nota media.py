numeros=[]
media=0
soma=0
for i in range(4):
    num = int(input("Digite as notas:"))
    numeros.append(num)
for num in numeros:
    soma= soma+num
media= soma/4
print(media)
if (media<4):
    print("esta reporvado")
elif (media>=4 and media<=7):
    print("esta de recuperação")
else:
    print("esta aprovado")
    