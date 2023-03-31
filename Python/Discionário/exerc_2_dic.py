from random import randint

def Somadados():
    dadoA = randint(1,6)
    dadoB = randint(1,6)
    soma = dadoA + dadoB  
    return(soma)
 
def imprimir(dic):
    for chaves,valor in dic.items():
        print(chaves,valor, valor*100/1000 ,"%")

def somaDemilNumeros():
    vezes=0
    somatoria = {
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0,
        10:0,
        11:0,
        12:0
    }
    for x in range(1000):
        soma = Somadados()
        somatoria[soma] = somatoria[soma] + 1
    imprimir(somatoria)
    
somaDemilNumeros()