def maiorsc(texto1, texto2):
    i = len(texto1)-1
    j = len(texto2)-1
    return msc(i,j,texto1,texto2)
def msc(i,j,texto1,texto2):
    if i<0 or j<0:
        return ""
    if texto1[i] == texto2[j]:
        return msc(i-1,j-1,texto1,texto2) + texto1[i]
    else:
        seq1 = msc(i-1,j,texto1, texto2)
        seq2=  msc(i, j-1, texto1, texto2)
        if len(seq1)>len(seq2):
            return seq1
        else:
            return seq2

print(maiorsc("xxxxxxxxace","yyyyyyyyadcbe"))