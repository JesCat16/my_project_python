n2 = open("numeros2.txt","r")
n = n2.readlines()
numeros = list(map(int,n))
soma=0

for elementos in numeros:
    soma = soma + elementos

print(soma)
n2.close()