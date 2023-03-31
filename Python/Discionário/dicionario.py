def procuraReversa(dic,val):
    chaves = []
    for chave , valor in dic.items():
        if valor == val:
            chaves.append(chave)
    print(chaves)

def main():
    d={
        1:'ola',
        2:'tudo',
        3:'bem',
        4:'ola',
        5:'com'
    }
    procuraReversa( d,'ola')

main()
