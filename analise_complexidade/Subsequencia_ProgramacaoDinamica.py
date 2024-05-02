def maiorsc(texto1, texto2):
    m = len(texto1)
    n = len(texto2)
    tb = [[0]*(n+1) for x in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if texto1[i-1] == texto2[j-1]:
                tb[i][j] = tb[i-1][j-1] + 1
            else:
                tb[i][j] = max(tb[i-1][j], tb[i][j-1])
    for x in tb:
        print(x)
    i, j = m,n
    palavra=""
    while i > 0 and j > 0:
        if texto1[i-1] == texto2[j-1]:
            palavra+= texto1[i-1]
            i -= 1
            j -= 1
        elif tb[i-1][j] > tb[i][j-1]:
            i -= i
        else:
            j -= 1
    print(palavra[::-1])

    

print(maiorsc("xxxxxace","yyyyyadcbe"))