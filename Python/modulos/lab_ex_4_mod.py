
def ordem(p ="string"):
    listap=p.split("-")
    listaorndenada = sorted(listap)
    return print(*listaorndenada, sep="-")

def mini(p ="string"):
    listap=p.split("-")
    minuscula=0
    maiuscula=0
    for p in range(len(listap)):
        for l in listap[p]:
            if l.islower():
                minuscula+=1
            else:
                maiuscula+=1
    return minuscula

def max(p ="string"):
    listap=p.split("-")
    minuscula=0
    maiuscula=0
    for p in range(len(listap)):
        for l in listap[p]:
            if l.islower():
                minuscula+=1
            else:
                maiuscula+=1
    return maiuscula