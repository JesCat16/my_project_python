from math import sqrt
def primos(limite):
    numeros=[]
    lista2=[]
    for i in range(limite + 1):
        numeros.append(i)
    
    for s in numeros:
        if s == 0 or s == 1:
            numeros[s] = 0
        else:
            lista2.append(s)
        
    
    for p in lista2:
        if p <= int(sqrt(limite)):
            for n in numeros:
                if n % p == 0 and n != p:
                    numeros[n] = 0
        else:
            break
    print(*numeros)

