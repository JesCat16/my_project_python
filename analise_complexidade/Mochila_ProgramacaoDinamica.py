def get_valor(tb,n):
    for i in range(len(tb)):
        for j in range(len(tb[i])):
            if tb [i][j] == n:
                return i,j
    return -1,-1

def mochila(itens, capacidade):
    n = len(itens)
    tb = [[0]* (capacidade+1) for x in range(n+1)] #coluna por linha...só no python

    for i in range(1,n+1):
        peso = itens[i-1][0]
        valor = itens[i-1][1]
        for j in range(0,capacidade+1):
            if peso <=j:
                tb[i][j] = max(tb[i-1][j], tb[i-1][j-peso]+valor)
            else:
                tb[i][j] = tb[i-1][j]
    for x in tb:
        print(x)      
    max_valor = tb[n][capacidade]
    while max_valor > 0:
        print(get_valor(tb,max_valor)[0])
        posicao = get_valor(tb,max_valor)
        max_valor = max_valor-itens[posicao[0]-1][1]

    # for u in range(1,n+1):
    #     for a in range(0,capacidade+1):
    #         if tb[u][a] > capacidade:
    #             y = tb[u][a] - a
                


    

itens = [[3,4],[2,3],[5,6],[4,5]]
capacidade = 5
print(mochila(itens,capacidade))