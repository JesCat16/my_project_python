from random import randint
cartela = {
    'B':0,
    'I':0,
    'N':0,
    'G':0,
    'O':0
}
lB=[]
lI=[]
lN=[]
lG=[]
lO=[]

for b in range(5):
    lB.append(randint(1,15))

for i in range(5):
    lI.append(randint(16,30))

for n in range(5):
    lN.append(randint(31,46))

for g in range(5):
    lG.append(randint(47,62))

for o in range(5):
    lO.append(randint(63,78))

cartela['B'] = lB
cartela['I'] = lI
cartela['N'] = lN
cartela['G'] = lG
cartela['O'] = lO

print(cartela)