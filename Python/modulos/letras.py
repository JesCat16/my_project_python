def capitalizador (lista):
    for indice in range(len(lista)-3):
        if indice == 0:
           lista = lista[indice].upper() + lista[1:]
        elif lista[indice] == "." or lista[indice] == "!" or lista[indice] == "?":
          lista = lista[:indice+2] + lista[indice+2].upper() + lista[indice+3:]
    return lista