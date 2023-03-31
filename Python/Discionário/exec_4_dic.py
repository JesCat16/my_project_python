def anagrama(p1,p2):
    palavras1 = {}
    palavras2 = {}

    for p in p1:
        if p not in palavras1:
            palavras1[p] = 1
        else:
            palavras1[p] = palavras1[p] + 1

    for l in p2:
        if l not in palavras2:
            palavras2[l] = 1
        else:
            palavras2[l] = palavras2[l] + 1
    if palavras1 == palavras2:
        print('anagrama')
    else: 
        print('não anagrama')

def main():   
    palavra1 = input("Digite: ")
    palavra2 = input("Digite: ")
    anagrama(palavra1,palavra2)

main()