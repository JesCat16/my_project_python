
def caracters(s):
    if len(s) >=4:
        return True
    else:
        return False
def Lminusculas(s):
    soma=0
    for indice in range(len(s)):
        if s[indice].islower():
            soma+=1
    if soma > 0:
        return True
    else:
        return False
def Lmaiuscula(s):
    soma=0
    for indice in range(len(s)):
        if s[indice].isupper():
            soma+=1
    if soma > 0:
        return True
    else:
        return False