for i in range(1, 21):
    if i == 13:
        continue
    print(i)


print("********************* 2º código*********************")

i = 20
while i >= 1:
    if i == 13:
        i -= 1
        continue
    print(i)
    i -= 1


print("********************* 3º código*********************")  

numeros = list(range(1, 21))
numeros.remove(13)
for i in reversed(numeros): # usando loop for juntamente com a função reversed que tem o objetivo nesse caso de colocar em ordem decrescente
    print(i)