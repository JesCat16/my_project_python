from random import randrange, choice

def numeros():
  n = []
  for i in range(3):
    n.append(randrange(9))
  return n


def letras():
  l=[]
  alphab =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
  for i in range(4):
    l.append(choice(alphab))
  return l

def placas(numeros,letras):
  placa=[]
  for i in range(7):
    if i <=2:
      placa.append(letras[i])
    elif i == 3:
      placa.append(numeros[0])
    elif i == 4:
      placa.append(letras[3])
    else:
      placa.append(numeros[i-4])
  return placa
