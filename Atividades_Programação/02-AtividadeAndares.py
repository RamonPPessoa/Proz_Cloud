#Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
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