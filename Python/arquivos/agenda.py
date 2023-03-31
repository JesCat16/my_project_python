contatos = open("contatos.txt","a")

while True:
    nome = input("Nome: ")
    if nome == "":
        break
    telefone = input("Telefone: ")
    contatos.write("%s %s\n" % (nome,telefone))
contatos.close()

contatos = open("contatos.txt","r")

completa = []

for linha in contatos.readlines():
    linha_separada = linha.split(" ")
    completa.append(linha_separada)
print(completa)
#nome
print(completa[0][0])
#telefone
print(completa[0][1])