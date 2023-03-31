pares = open("pares.txt","w")

for n in range(1,1000):
    if n % 2 == 0:
        pares.write("%d\n" % n)
pares.close()
