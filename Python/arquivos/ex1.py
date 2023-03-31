pares = open("pares.txt","r")
pares_invertido = open("pares_invertido.txt","w")

conteudo = pares.readlines()
print(conteudo)
invertida = conteudo[::-1]

for elemento in invertida:
    pares_invertido.write(elemento)

pares.close()
pares_invertido.close()