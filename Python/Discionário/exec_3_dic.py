palavra='sdfghjklçiuhygtfrdssdfghjkikjhfdf'

dicionario = {}

for caracter in palavra:
    if caracter not in dicionario:
        dicionario[caracter] = 1
    else:
        dicionario[caracter] = dicionario[caracter] + 1

print(dicionario)
print(len(dicionario))

