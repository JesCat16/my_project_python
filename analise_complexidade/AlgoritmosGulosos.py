def greedy_selector(s,f,n):
    A = []
    tupla = [s[0],f[0]]
    A.append(tupla)
    k = 0
    m = 1
    for m in range(n):
        if s[m] >= f[k]:
            tupla = [s[m],f[m]]
            A.append(tupla)
            k = m
        else:
            m=m+1
    return A

def mochila(itens,capacidade,n):
    itens.sort(key=lambda x:x[0]/x[1])
    i=0
    total = 0
    for i in range(0,n):
        peso = itens[i][0]
        valor = itens[i][1]
        if peso <= capacidade:
            total+=valor
            capacidade-=peso
        else:
            total += valor * (capacidade/peso)
            capacidade = 0
        if capacidade == 0:
            return total
    
itens = [[30,20],[10,60],[20,100]]
capacidade = 50
print(mochila(itens,capacidade,len(itens)))



# s = [1,3,0,5,3,5,6,7,8,2,12]
# f = [4,5,6,7,9,9,10,11,12,14,16]
# n = 11
# print(greedy_selector(s,f,n))

